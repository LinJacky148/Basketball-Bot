# 所有球隊排名
import requests
from opencc import OpenCC
from fuzzywuzzy import fuzz


def GetAllTeamStandings():
    url = "https://china.nba.cn/stats2/season/conferencestanding.json?locale=zh_CN"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        standing_groups = data.get("payload", {}).get("standingGroups", [])

        if not standing_groups:
            return "沒有找到隊伍排名信息。"

        result_message = ""
        cc = OpenCC("s2t")  # 創建一個簡繁轉換器

        for standing_group in standing_groups:
            teams = standing_group.get("teams", [])
            for team in teams:
                profile = team.get("profile", {})
                standings = team.get("standings", {})

                if profile and standings:
                    Team_Name = "{}{}".format(
                        cc.convert(profile.get("city", "")),  # 轉換為繁體字
                        cc.convert(profile.get("displayAbbr", "")),  # 轉換為繁體字
                    )
                    Team_Rank = "{}排名#{}".format(
                        cc.convert(profile.get("displayConference", "")),  # 轉換為繁體字
                        standings.get("confRank", ""),
                    )
                    Team_WL = "{}勝-{}負".format(
                        standings.get("wins", ""), standings.get("losses", "")
                    )

                    result_message += (
                        "隊伍: {}\n排名: {}\n戰績: {}\n------------------\n".format(
                            Team_Name, Team_Rank, Team_WL
                        )
                    )
                else:
                    result_message += "無效的隊伍資料。\n"

        return result_message
    else:
        return "HTTP 請求失敗，狀態碼: {}".format(response.status_code)


# 單一球隊的排名

import requests
import opencc  # 載入 OpenCC 函式庫

# 創建OpenCC實例，設置轉換方式（從簡體字轉換成繁體字）
converter = opencc.OpenCC("s2twp")


def GetTeamStanding(team_name):
    base_url = "https://china.nba.cn/stats2/team/standing.json?locale=zh_CN&teamCode={}"
    team_code = None

    if team_name.lower() == "老鷹" or team_name.lower() == "hawks":
        team_code = "hawks"
    elif (
        team_name.lower() == "塞爾提克"
        or team_name.lower() == "celtics"
        or team_name.lower() == "bos"
    ):
        team_code = "celtics"
    elif team_name.lower() == "公牛" or team_name.lower() == "bulls":
        team_code = "bulls"
    elif team_name.lower() == "黃蜂" or team_name.lower() == "hornets":
        team_code = "hornets"
    elif team_name.lower() == "籃網" or team_name.lower() == "nets":
        team_code = "nets"
    elif team_name.lower() == "騎士" or team_name.lower() == "cavaliers":
        team_code = "cavaliers"
    elif team_name.lower() == "熱火" or team_name.lower() == "heat":
        team_code = "heat"
    elif team_name.lower() == "尼克" or team_name.lower() == "knicks":
        team_code = "knicks"
    elif team_name.lower() == "活塞" or team_name.lower() == "pistons":
        team_code = "pistons"
    elif team_name.lower() == "魔術" or team_name.lower() == "magic":
        team_code = "magic"
    elif team_name.lower() == "76人" or team_name.lower() == "76ers":
        team_code = "76ers"
    elif team_name.lower() == "七六人" or team_name.lower() == "76ers":
        team_code = "76ers"
    elif (
        team_name.lower() == "溜馬"
        or team_name.lower() == "pacers"
        or team_name.lower() == "ind"
    ):
        team_code = "pacers"
    elif (
        team_name.lower() == "巫師"
        or team_name.lower() == "wizards"
        or team_name.lower() == "was"
    ):
        team_code = "wizards"
    elif team_name.lower() == "暴龍" or team_name.lower() == "raptors":
        team_code = "raptors"
    elif team_name.lower() == "公鹿" or team_name.lower() == "bucks":
        team_code = "bucks"
    elif team_name.lower() == "獨行俠" or team_name.lower() == "mavericks":
        team_code = "mavericks"
    elif team_name.lower() == "金塊" or team_name.lower() == "nuggets":
        team_code = "nuggets"
    elif team_name.lower() == "勇士" or team_name.lower() == "warriors":
        team_code = "warriors"
    elif team_name.lower() == "火箭" or team_name.lower() == "rockets":
        team_code = "rockets"
    elif team_name.lower() == "灰狼" or team_name.lower() == "timberwolves":
        team_code = "timberwolves"
    elif (
        team_name.lower() == "快艇"
        or team_name.lower() == "clippers"
        or team_name.lower() == "lac"
    ):
        team_code = "clippers"
    elif team_name.lower() == "灰熊" or team_name.lower() == "grizzlies":
        team_code = "grizzlies"
    elif team_name.lower() == "雷霆" or team_name.lower() == "thunder":
        team_code = "thunder"
    elif team_name.lower() == "湖人" or team_name.lower() == "lakers":
        team_code = "lakers"
    elif team_name.lower() == "鵜鶘" or team_name.lower() == "pelicans":
        team_code = "pelicans"
    elif team_name.lower() == "拓荒者" or team_name.lower() == "blazers":
        team_code = "blazers"
    elif team_name.lower() == "太陽" or team_name.lower() == "suns":
        team_code = "suns"
    elif team_name.lower() == "馬刺" or team_name.lower() == "spurs":
        team_code = "spurs"
    elif team_name.lower() == "爵士" or team_name.lower() == "jazz":
        team_code = "jazz"
    elif team_name.lower() == "國王" or team_name.lower() == "kings":
        team_code = "kings"

    if team_code:
        url = base_url.format(team_code)
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if "payload" in data and data["payload"] is not None:
                team_data = data["payload"]["team"]
                profile = team_data.get("profile", {})
                standings = team_data.get("standings", {})
                coach = team_data.get("coach", {})

                Team_Rank = "{}排名#{}".format(
                    converter.convert(profile.get("displayConference", "")),  # 轉換為繁體字
                    standings.get("confRank", ""),
                )
                Team_WL = "{}勝-{}負".format(
                    standings.get("wins", ""), standings.get("losses", "")
                )

                result_message = "隊伍: {}\n排名: {}\n戰績: {}".format(
                    converter.convert(profile.get("displayAbbr", "")),  # 轉換為繁體字
                    Team_Rank,
                    Team_WL,
                )
                return result_message

        # 如果未找到指定隊伍或資料為空
        return "找不到隊伍: {}\n".format(team_name)

    return "找不到隊伍: {}\n".format(team_name)
