# 各球隊陣容
import requests
import opencc

# 創建OpenCC實例，設置轉換方式
converter = opencc.OpenCC("s2twp")


def GetTeamRoster(team_code):
    # 使用全局變數的網址模板，並替換teamCode
    url = f"https://china.nba.cn/stats2/team/roster.json?locale=zh_CN&teamCode={team_code}"
    response = requests.get(url)

    # 檢查請求是否成功
    if response.status_code == 200:
        try:
            # 解析JSON數據
            roster_data = response.json()

            # 檢查JSON數據是否包含球員信息
            if "payload" in roster_data and "players" in roster_data["payload"]:
                players_data = roster_data["payload"]["players"]
                player_info_list = []

                # 球員數據
                for player_data in players_data:
                    player_info = {}
                    player_info["displayName"] = converter.convert(
                        player_data["profile"]["displayName"]
                    )
                    player_info["position"] = player_data["profile"]["position"]
                    player_info["height"] = player_data["profile"]["height"]
                    player_info["weight"] = player_data["profile"]["weight"]
                    player_info["jerseyNo"] = player_data["profile"]["jerseyNo"]
                    player_info_list.append(player_info)

                return player_info_list
            else:
                print("未找到球員信息")
                return None
        except Exception as e:
            print(f"解析JSON時發生錯誤: {e}")
            return None
    else:
        print(f"請求失敗，HTTP 狀態碼: {response.status_code}")
        return None
