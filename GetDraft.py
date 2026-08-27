import requests
import json
from opencc import OpenCC

def GetAllDraftInfo():
    url ="https://china.nba.cn/feeds/DraftPicks/draftpicks.json"

    response = requests.get(url)
    cc = OpenCC('s2t')  # 簡體轉繁體

    if response.status_code == 200:
        data = json.loads(response.text)  # JSON數據

        info_text = cc.convert("NBA 2023年選秀資訊:\n\n")
        current_round = 0

        # 遍歷每個選秀資訊
        for pick in data:
            # 檢查是否新的一輪
            if pick["Round"] != current_round:
                current_round = pick["Round"]
                info_text += cc.convert("\n---------- 第{}輪 ----------\n").format(current_round)

            pick_number = pick["PickNo"]
            team_city = pick["TeamCity"]
            team_name = pick["TeamName"]
            player_name = pick["PlayerName"]
            from_place = pick["From"]
            height = pick["Height"]
            weight = pick["Weight"]
            position = pick["Position"]

            line = f"第{pick_number}順位: {team_city} {team_name} - {player_name}, 來自{from_place}, 身高{height}, 體重{weight}磅, 位置{position}\n"
            info_text += cc.convert(line)

        return info_text
    else:
        return cc.convert("無法獲取選秀資訊。")





import requests
import json
from opencc import OpenCC

def GetDraftInfoByPickNumber(pick_number):
    url ="https://china.nba.cn/feeds/DraftPicks/draftpicks.json"
    cc = OpenCC('s2t')  # 簡體轉繁體

    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.text)

        # 搜索指定順位的選秀
        for pick in data:
            if pick["PickNo"] == pick_number:
                team_city = cc.convert(pick["TeamCity"])
                team_name = cc.convert(pick["TeamName"])
                player_name = cc.convert(pick["PlayerName"])
                from_place = cc.convert(pick["From"])
                height = cc.convert(pick["Height"])
                weight = pick["Weight"]
                position = cc.convert(pick["Position"])

                return (
                    f"2023年第{pick_number}順位選秀是: {team_city} {team_name} - {player_name}, "
                    f"來自{from_place}, 身高{height}, 體重{weight}磅, 位置{position}"
                )

        return cc.convert(f"未找到2023年第{pick_number}順位的選秀信息。")
    else:
        return cc.convert("無法取得選秀資訊。")
