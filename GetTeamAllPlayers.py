# 單一球隊所有球員
import json, requests
def GetTeamAllPlayers(Team):
    url ="https://china.nba.cn/stats2/team/playerstats.json?countryCode=CN&locale=zh_CN&teamCode={}".format(
        Team
    )
    Data = json.loads(requests.get(url).text)["payload"]
    Data_TeamProfile = Data["team"]["profile"]
    Data_TeamStanding = Data["team"]["standing"]
    Players = Data["team"]["players"]

    TeamPlayers = json.load(open("json/Player/TeamPlayers.json", "r", encoding="utf-8"))
    TeamInfo = TeamPlayers["body"]["contents"][0]["contents"]
    TeamInfo_ = TeamInfo[1]["contents"]
    PlayerBox = TeamPlayers["body"]["contents"]

    TeamInfo[0][
        "url"
    ] ="https://china.nba.cn/media/img/teams/logos/{}_logo.png".format(
        Data_TeamProfile["abbr"]
    )
    TeamInfo_[0]["text"] = "{}{}".format(
        Data_TeamProfile["city"], Data_TeamProfile["displayAbbr"]
    )
    TeamInfo_[1]["text"] = "{}排名#{}".format(
        Data_TeamProfile["displayConference"], Data_TeamStanding["confRank"]
    )
    TeamInfo_[2]["text"] = "{}勝-{}負".format(
        Data_TeamStanding["wins"], Data_TeamStanding["losses"]
    )

    Seperater = json.load(open("json/Player/Seperater.json", "r", encoding="utf-8"))

    for Player in Players:
        PlayerProfile = Player["profile"]
        PlayerOut = json.load(open("json/Player/Player.json", "r", encoding="utf-8"))
        PlayerInfo = PlayerOut["contents"]
        PlayerInfo[0]["text"] = "{} {}".format(
            PlayerProfile["firstName"], PlayerProfile["lastName"]
        )
        PlayerInfo[1]["text"] = PlayerProfile["jerseyNo"]
        PlayerInfo[2]["action"]["data"] = "SelectPlayerName {}".format(
            PlayerProfile["code"]
        )
        PlayerBox.append(Seperater)
        PlayerBox.append(PlayerOut)
    return TeamPlayers
