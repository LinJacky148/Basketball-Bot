# 各球隊賽程資訊
import requests
from opencc import OpenCC

def convert_to_traditional_chinese(simplified_chinese):
    cc = OpenCC("s2twp")  # 使用 s2twp 轉換器，從簡體轉換成繁體（台灣標準）
    return cc.convert(simplified_chinese)

def GetAllTeamSchedules(team_code, target_month):
    url = f"https://china.nba.cn/stats2/team/schedule.json?countryCode=CN&locale=zh_CN&teamCode={team_code}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        month_groups = data["payload"]["monthGroups"]

        team_schedules = {}  # 存儲比賽信息的字典

        for month_group in month_groups:
            games = month_group["games"]

            for game in games:
                game_date_time = game["profile"]["dateTimeEt"]
                game_date = game_date_time.split("T")[0]
                game_month = int(game_date.split("-")[1])

                if game_month == target_month:
                    home_team_name = convert_to_traditional_chinese(
                        game["homeTeam"]["profile"]["name"]
                    )
                    away_team_name = convert_to_traditional_chinese(
                        game["awayTeam"]["profile"]["name"]
                    )
                    game_time = game_date_time.split("T")[1]
                    arena_name = convert_to_traditional_chinese(
                        game["profile"]["arenaName"]
                    )

                    # 構建比賽信息字串
                    game_info = f"日期：{game_date}，時間：{game_time}，主隊：{home_team_name}，客隊：{away_team_name}，球場：{arena_name}"

                    # 如果主隊名稱不在字典中，則創建一個新的主隊項目
                    if home_team_name not in team_schedules:
                        team_schedules[home_team_name] = []

                    # 如果客隊名稱不在字典中，則創建一個新的客隊項目
                    if away_team_name not in team_schedules:
                        team_schedules[away_team_name] = []

                    # 添加比賽信息到主隊和客隊的列表中
                    team_schedules[home_team_name].append(game_info)
                    team_schedules[away_team_name].append(game_info)

        return team_schedules
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None
