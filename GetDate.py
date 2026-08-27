# 今日賽事 過去賽事查詢
# 台灣時間會和美國時間差一天，以美國為主
import requests
from datetime import datetime, timedelta
from pytz import timezone
from pytz import timezone, utc


ESPN_API_ENDPOINT = (
    "https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard"
)
ESPN_API_KEY = "YOUR_ESPN_API_KEY"


# 設定 ESPN API 的時區為美國東部時區
espn_timezone = timezone("US/Eastern")

# 設定台灣時區
taiwan_timezone = timezone("Asia/Taipei")


def convert_to_taiwan_time(dt):
    taiwan_time = dt.astimezone(taiwan_timezone)
    taiwan_time = taiwan_timezone.normalize(taiwan_time)  # 進行時區的正規化
    return taiwan_time.strftime("%Y-%m-%d %H:%M:%S")


def get_nba_games_info():
    response = requests.get(ESPN_API_ENDPOINT)

    if response.status_code == 200:
        data = response.json()
        today = datetime.now()

        if "events" in data:
            games_today = [
                game
                for game in data["events"]
                if datetime.fromisoformat(game["date"]).astimezone(taiwan_timezone)
                >= taiwan_timezone.localize(today)
            ]

            if games_today:
                games_info = ""

                for game in games_today:
                    team1 = game["competitions"][0]["competitors"][0]["team"][
                        "displayName"
                    ]
                    team2 = game["competitions"][0]["competitors"][1]["team"][
                        "displayName"
                    ]

                    game_date = (
                        datetime.fromisoformat(game["date"])
                        .astimezone(taiwan_timezone)
                        .strftime("%Y-%m-%d %H:%M:%S")
                    )
                    venue = game["competitions"][0]["venue"]["fullName"]
                    game_status = game["status"]["type"]["description"]

                    games_info += f"{team1} vs {team2}\n"
                    games_info += f"日期時間: {game_date}\n"
                    games_info += f"比賽地點: {venue}\n"
                    games_info += f"比賽狀態: {game_status}\n\n"

                return f"今日有比賽:\n{games_info}"

            else:
                future_games = [
                    game
                    for game in data["events"]
                    if datetime.fromisoformat(game["date"]).astimezone(taiwan_timezone)
                    > taiwan_timezone.localize(today)
                ]

                if future_games:
                    next_game = future_games[0]
                    next_game_date = (
                        datetime.fromisoformat(next_game["date"])
                        .astimezone(taiwan_timezone)
                        .strftime("%Y-%m-%d %H:%M:%S")
                    )
                    return f"今日無比賽，下場比賽於 {next_game_date}"
                else:
                    return "目前沒有未來的賽事資訊。"

        else:
            return "API 响應中未找到 NBA 賽事資訊。"


# 定義 ESPN API 的時區為美國東部時區
espn_timezone = timezone("US/Eastern")

# 定義台灣時區
taiwan_timezone = timezone("Asia/Taipei")


def convert_to_taiwan_time(dt):
    # 將日期時間轉換為 UTC 時間
    dt_utc = dt.astimezone(utc)

    # 將 UTC 時間轉換為台灣時區
    dt_taiwan = dt_utc.astimezone(taiwan_timezone)

    # 格式化台灣時間
    return dt_taiwan.strftime("%Y-%m-%d %H:%M:%S")


def get_games(date=None):
    params = {"apikey": ESPN_API_KEY, "dates": date if date else ""}
    response = requests.get(ESPN_API_ENDPOINT, params=params)
    data = response.json()

    games = []
    today = datetime.now()

    for event in data.get("events", []):
        team1 = event["competitions"][0]["competitors"][0]["team"]["displayName"]
        team2 = event["competitions"][0]["competitors"][1]["team"]["displayName"]

        # 獲取比分資訊，並將分數轉換為整數
        team1_score = int(event["competitions"][0]["competitors"][0]["score"])
        team2_score = int(event["competitions"][0]["competitors"][1]["score"])

        # 比較得分確定贏家
        if team1_score > team2_score:
            winner = team1
        elif team1_score < team2_score:
            winner = team2
        else:
            winner = "平局"

        # 處理比賽日期和時間
        game_date = datetime.fromisoformat(event["date"])
        game_date_formatted = convert_to_taiwan_time(game_date)

        # 添加比賽信息到列表中
        game_info = f"{team1} {team1_score} - {team2_score} {team2}, 贏家: {winner}\n"
        game_info += f"日期時間: {game_date_formatted}\n"

        # 提取统计数据和领先球员信息（每支队伍）
        for competitor in event["competitions"][0]["competitors"]:
            # 提取leaders訊息
            leaders = competitor["leaders"]
            for leader in leaders:
                stat_name = leader["name"]
                stat_display_name = leader["displayName"]
                leader_name = leader["leaders"][0]["athlete"]["displayName"]
                leader_value = leader["leaders"][0]["displayValue"]

                # 檢查是否為我們關心的類型
                if stat_name in ["points", "rebounds", "assists", "rating"]:
                    game_info += (
                        f"{stat_display_name}領先球員: {leader_name} ({leader_value})\n"
                    )

        games.append(game_info)

    return games


from datetime import datetime, timedelta
import requests


def get_next_game_date():
    for i in range(1, 30):  # 最多查找未來30天
        future_date = (datetime.date.today() + timedelta(days=i)).strftime("%Y%m%d")
        params = {"apikey": ESPN_API_KEY, "dates": future_date}
        response = requests.get(ESPN_API_ENDPOINT, params=params)
        data = response.json()
        if data.get("events", []):  # 如果那天有比賽
            return future_date[4:6] + "/" + future_date[6:8]  # 返回MM/DD的格式
    return None


def get_past_games(date):
    games = get_games(date)  # 需要實現 get_games 函式
    if games:
        return "\n".join(games)
    else:
        return f"{date} 無賽事。"


def get_future_games():
    return get_next_game_date()
