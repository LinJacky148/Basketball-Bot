# 載入LineBot所需要的模組
import re
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
from linebot.models import FlexSendMessage
from linebot.models import (
    MessageEvent,
    TextSendMessage,
    ImageSendMessage,
    TemplateSendMessage,
    ButtonsTemplate,
    MessageTemplateAction,
    PostbackEvent,
    PostbackTemplateAction,
    LocationSendMessage,
)

# 載入flask模組
from flask import Flask, request, abort

# 讀取模組
import json

# 外部函數模組
from function.GetTeamSchedules import *
from function.GetBasketballNews import *
from function.GetDate import *
from function.GetAllTeamStandings import *
from function.random_statement import *
from function.FreeMarket import *
from function.GetDraft import *
from function.TeamNews import *
from function.Blogs import *
from function.GetData import *
from function.GetTeamRoster import *
from function.GetNBAData import *
from function.GetTeam import *
from function.GetTeamAllPlayers import *
from function.GetPlayer import *

# bert模組
from predict import bert


app = Flask(__name__)
line_bot_api = LineBotApi(
    "B2Pm2vlZgh96tdDoB797o9H/OxuIvYHZL6x1OtjD3qCK+ylC8487TBo0XA7wBPIbgmjOP9RDijajX3OlQvWVUlkuZe6a9vaTwxkfGEVnBFgpIFtBPgUxw1jydYhfOYV3t3MGbgB8GtuQOgYsBlFC/wdB04t89/1O/w1cDnyilFU="
)
handler = WebhookHandler("e53182d29570ead6964c8f03e72cdd0d")


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=["POST"])
def callback():
    # get X-Line-Signature header value
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # 將訊息轉換為 json 格式並儲存文字
    json_data = json.loads(body)
    with open("./data.json", "a", encoding="utf8") as fp:
        json.dump(json_data, fp, indent=3, ensure_ascii=False)  # 自動換行 轉換編碼Flase
        fp.write("\n")  # json自動空行
    # print( "類別:" +json_data['events'][0]['type'] )  #確認類別
    # print( "文字: " + json_data['events'][0]['message']['text'] ,"\n目的地: " +json_data['destination'] )
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return "OK"



# 訊息傳遞區塊
##### 基本上程式編輯都在這個function
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print(event.message.text)
    # 不經過bert 可能用於圖文選單

    if event.message.text == '明星球員數據':
        try:
            message = TextSendMessage(
                text='請選擇球員',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="LeBronJames", text="LeBronJames")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="KevinDurant", text="KevinDurant")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="JamesHarden", text="JamesHarden")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="KawhiLeonard", text="KawhiLeonard")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="GiannisAntetokounmpo", text="GiannisAntetokounmpo")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="StephenCurry", text="StephenCurry")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="AnthonyDavis", text="AnthonyDavis")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="JoelEmbiid", text="JoelEmbiid")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="NikolaJokic", text="NikolaJokic")
                        ),
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
##############################################LeBronJames###################################################################
    if event.message.text == 'LeBronJames':
        try:
            message = TextSendMessage(
                text='請選擇賽季',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="2003-04~2012-13賽季", text="2003-04~2012-13賽季")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2014-15~2022-23賽季", text="2014-15~2022-23賽季")
                        ),
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

    if event.message.text == '2003-04~2012-13賽季':
        try:
            message = TextSendMessage(
                text='請選擇賽季',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="2003-04 (CLE)", text="2003-04 (CLE)\n平均得分: 20.9\n平均籃板: 5.5\n平均助攻: 5.9\n投籃命中率: 41.7%\n三分命中率: 29.0%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2004-05 (CLE)", text="2004-05 (CLE)\n平均得分: 27.2\n平均籃板: 7.\n平均助攻: 7.2\n投籃命中率: 47.2%\n三分命中率: 35.1%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2005-06 (CLE)", text="2005-06 (CLE)\n平均得分: 31.4\n平均籃板: 7.0\n平均助攻: 6.6\n投籃命中率: 48.0%\n三分命中率: 33.5%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2006-07 (CLE)", text="2006-07 (CLE)\n平均得分: 27.3\n平均籃板: 6.7\n平均助攻: 6.0\n投籃命中率: 47.6%\n三分命中率: 31.9%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2007-08 (CLE)", text="2007-08 (CLE)\n平均得分: 30.0\n平均籃板: 7.9\n平均助攻: 7.2\n投籃命中率: 48.4%\n三分命中率: 31.5%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2008-09 (CLE)", text="2008-09 (CLE)\n平均得分: 28.4\n平均籃板: 7.6\n平均助攻: 7.2\n投籃命中率: 48.9%\n三分命中率: 34.4%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2008-09 (CLE)", text="2008-09 (CLE)\n平均得分: 29.7\n平均籃板: 7.3\n平均助攻: 8.6\n投籃命中率: 50.3%\n三分命中率: 33.3%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2008-09 (CLE)", text="2008-09 (CLE)\n平均得分: 26.7\n平均籃板: 7.5\n平均助攻: 7.0\n投籃命中率: 51.0%\n三分命中率: 33.0%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2008-09 (CLE)", text="2008-09 (CLE)\n平均得分: 27.1\n平均籃板: 7.9\n平均助攻: 6.2\n投籃命中率: 53.1%\n三分命中率: 36.2%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2012-13 (MIA)", text="平均得分: 26.8\n平均籃板: 8.0\n平均助攻: 7.3\n投籃命中率: 56.5%\n三分命中率: 40.6%")
                        ),  
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
    if event.message.text == '2014-15~2022-23賽季':
        try:
            message = TextSendMessage(
                text='請選擇賽季',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="2014-15 (CLE)", text="2014-15 (CLE)\n平均得分: 25.3\n平均籃板: 6.0\n平均助攻: 7.4\n投籃命中率: 48.8%\n三分命中率: 35.4%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2015-16 (CLE)", text="2015-16 (CLE)\n平均得分: 25.3\n平均籃板: 7.4\n平均助攻: 6.8\n投籃命中率: 52.0%\n三分命中率: 30.9%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2016-17 (CLE)", text="2016-17 (CLE)\n平均得分: 26.4\n平均籃板: 8.6\n平均助攻: 8.7\n投籃命中率: 54.8%\n三分命中率: 36.3%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2017-18 (CLE)", text="2017-18 (CLE)\n平均得分: 27.5\n平均籃板: 8.6\n平均助攻: 9.1\n投籃命中率: 54.2%\n三分命中率: 36.7%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2018-19 (LAL)", text="2018-19 (LAL)\n平均得分: 27.4\n平均籃板: 8.5\n平均助攻: 8.3\n投籃命中率: 51.0%\n三分命中率: 33.9%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2019-20 (LAL)", text="2019-20 (LAL)\n平均得分: 25.3平均籃板: 7.8\n平均助攻: 10.2\n投籃命中率: 49.3%\n三分命中率: 34.8%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2020-21 (LAL)", text="2020-21 (LAL)\n平均得分: 25.0\n平均籃板: 7.7\n平均助攻: 7.8\n投籃命中率: 51.3%\n三分命中率: 36.5%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2021-22 (LAL)", text="2021-22 (LAL)\n平均得分: 30.3\n平均籃板: 8.2\n平均助攻: 6.2\n投籃命中率: 52.4%\n三分命中率: 35.9%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2022-23 (LAL)", text="2022-23 (LAL)\n平均得分: 28.9\n平均籃板: 8.3\n平均助攻: 6.8\n投籃命中率: 50.0%\n三分命中率: 32.1%")
                        ),
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
###################################KevinDurant#############################################################################
    if event.message.text == 'KevinDurant':
        try:
            message = TextSendMessage(
                text='請選擇賽季',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="*2007-08~2014-15賽季", text="*2007-08~2014-15賽季")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="*2015-16~2022-23賽季", text="*2015-16~2022-23賽季")
                        ),
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

    if event.message.text == '*2007-08~2014-15賽季':
        try:
            message = TextSendMessage(
                text='請選擇賽季',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="2007-08 (SEA)", text="2007-08 (SEA)\n平均得分: 20.3\n平均籃板: 4.4\n平均助攻: 2.4投\n籃命中率: 43.0%\n三分命中率: 28.8%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2008-09 (OKC)", text="2008-09 (OKC)\n平均得分: 25.3\n平均籃板: 6.5\n平均助攻: 2.8\n投籃命中率: 47.6%\n三分命中率: 42.2%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2009-10 (OKC)", text="2009-10 (OKC)\n平均得分: 30.1\n平均籃板: 7.\n平均助攻: 2.8\n投籃命中率: 47.6%\n三分命中率: 36.5%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2010-11 (OKC)", text="2010-11 (OKC)\n平均得分: 27.7\n平均籃板: 6.8\n平均助攻: 2.7\n投籃命中率: 46.2%\n三分命中率: 35.0%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2011-12 (OKC)", text="2011-12 (OKC)\n平均得分: 28.0\n平均籃板: 8.0\n平均助攻: 3.5\n投籃命中率: 49.6%\n三分命中率: 38.7%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2012-13 (OKC)", text="2012-13 (OKC)\n平均得分: 28.1\n平均籃板: 7.9\n平均助攻: 4.6\n投籃命中率: 51.0%\n三分命中率: 41.6%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2013-14 (OKC)", text="2013-14 (OKC)\n平均得分: 32.0\n平均籃板: 7.4\n平均助攻: 5.5\n投籃命中率: 50.3%\n三分命中率: 39.1%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2014-15 (OKC)", text="2014-15 (OKC)\n平均得分: 25.4\n平均籃板: 6.6\n平均助攻: 4.1\n投籃命中率: 51.0%\n三分命中率: 40.3%")
                        ),
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
    if event.message.text == '*2015-16~2022-23賽季':
        try:
            message = TextSendMessage(
                text='請選擇賽季',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="2015-16 (OKC)", text="2015-16 (OKC)\n平均得分: 28.2\n平均籃板: 8.2\n平均助攻: 5.0\n投籃命中率: 50.5%\n三分命中率: 38.7%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2016-17 (GSW)", text="2016-17 (GSW)\n平均得分: 25.1\n平均籃板: 8.3\n平均助攻: 4.8\n投籃命中率: 53.7%\n三分命中率: 37.5%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2017-18 (GSW)", text="2017-18 (GSW)\n平均得分: 26.4\n平均籃板: 6.8\n平均助攻: 5.4\n投籃命中率: 51.6%\n三分命中率: 41.9%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2018-19 (GSW)", text="2018-19 (GSW)\n平均得分: 26.0\n平均籃板: 6.4\n平均助攻: 5.9\n投籃命中率: 52.1%\n三分命中率: 35.3%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2020-21 (BRK)", text="2020-21 (BRK)\n平均得分: 26.9\n平均籃板: 7.1\n平均助攻: 5.6\n投籃命中率: 53.7%\n三分命中率: 45.0%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2021-22 (BRK)", text="2021-22 (BRK)\n平均得分: 29.9\n平均籃板: 7.4\n平均助攻: 6.4\n投籃命中率: 51.8%\n三分命中率: 38.3%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2022-23 ", text="2022-23\n平均得分: 29.1\n平均籃板: 6.7\n平均助攻: 5.0\n投籃命中率: 56.0%\n三分命中率: 40.4%")
                        ),
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

    #######################################JamesHarden###############################################################################
    if event.message.text == 'JamesHarden':
        try:
            message = TextSendMessage(
                text='請選擇賽季',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="2009-10~2017-18賽季", text="2009-10~2017-18賽季")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2018-19~2022-23賽季", text="2018-19~2022-23賽季")
                        ),
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

    if event.message.text == '2009-10~2017-18賽季':
        try:
            message = TextSendMessage(
                text='請選擇賽季',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="2009-10 (OKC)", text="2009-10 (OKC)\n平均得分: 9.9\n平均籃板: 3.2\n平均助攻: 1.8\n投籃命中率: 40.3%\n三分命中率: 37.5%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2010-11 (OKC)", text="2010-11 (OKC)\n平均得分: 12.2\n平均籃板: 3.1\n平均助攻: 2.1\n投籃命中率: 43.6%\n三分命中率: 34.9%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2011-12 (OKC)", text="2011-12 (OKC)\n平均得分: 16.8\n平均籃板: 4.1\n平均助攻: 3.7\n投籃命中率: 49.1%\n三分命中率: 39.0%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2012-13 (HOU)", text="2012-13 (HOU)\n平均得分: 25.9\n平均籃板: 4.9\n平均助攻: 5.8\n投籃命中率: 43.8%\n三分命中率: 36.8%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2013-14 (HOU)", text="2013-14 (HOU)\n平均得分: 25.4\n平均籃板: 4.7\n平均助攻: 6.1\n投籃命中率: 45.6%\n三分命中率: 36.6%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2014-15 (HOU)", text="2014-15 (HOU)\n平均得分: 27.4\n平均籃板: 5.7\n平均助攻: 7.0\n投籃命中率: 44.0%\n三分命中率: 37.5%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2015-16 (HOU)", text="2015-16 (HOU)\n平均得分: 29.0\n平均籃板: 6.1\n平均助攻: 7.5\n投籃命中率: 43.9%\n三分命中率: 35.9%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2016-17 (HOU)", text="2016-17 (HOU)\n平均得分: 29.1\n平均籃板: 8.1\n平均助攻: 11.2\n投籃命中率: 44.0%\n三分命中率: 34.7%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2017-18 (HOU)", text="2017-18 (HOU)\n平均得分: 30.4\n平均籃板: 5.4\n平均助攻: 8.8\n投籃命中率: 44.9%\n三分命中率: 36.7%")
                        ),
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
    if event.message.text == '2018-19~2022-23賽季':
        try:
            message = TextSendMessage(
                text='請選擇賽季',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="2018-19 (HOU)", text="2018-19 (HOU)\n平均得分: 36.1\n平均籃板: 6.6\n平均助攻: 7.5\n投籃命中率: 44.2%\n三分命中率: 36.8%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2019-20 (HOU)", text="2019-20 (HOU)\n平均得分: 34.3\n平均籃板: 6.6\n平均助攻: 7.5\n投籃命中率: 44.4%\n三分命中率: 35.5%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2020-21 (TOT)", text="2020-21 (TOT)\n平均得分: 24.6\n平均籃板: 7.9\n平均助攻: 10.8\n投籃命中率: 46.6%\n三分命中率: 36.2%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2021-22 (TOT)", text="2021-22 (TOT)\n平均得分: 22.0\n平均籃板: 7.7\n平均助攻: 10.3\n投籃命中率: 41.0%\n三分命中率: 33.0%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2022-23 (PHI)", text="2022-23 (PHI)\n平均得分: 21.0\n平均籃板: 6.1\n平均助攻: 10.7\n投籃命中率: 44.1%\n三分命中率: 38.5%")
                        ),
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
#####################################################KawhiLeonard#######################################################################################
    if event.message.text == 'KawhiLeonard':
        try:
            message = TextSendMessage(
                text='請選擇2011-12~2022-23賽季',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="2011-12 (SAS)", text="2011-12 (SAS)\n平均得分: 7.9\n平均籃板: 5.1\n平均助攻: 1.1\n投籃命中率: 49.3%\n三分命中率: 37.6%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2012-13 (SAS)", text="2012-13 (SAS)\n平均得分: 11.9\n平均籃板: 6.0\n平均助攻: 1.6\n投籃命中率: 49.4%\n三分命中率: 37.4%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2013-14 (SAS)", text="2013-14 (SAS)\n平均得分: 12.8\n平均籃板: 6.2\n平均助攻: 2.0\n投籃命中率: 52.2%\n三分命中率: 37.9%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2014-15 (SAS)", text="2014-15 (SAS)\n平均得分: 16.5\n平均籃板: 7.2\n平均助攻: 2.5\n投籃命中率: 47.9%\n三分命中率: 34.9%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2015-16 (SAS)", text="2015-16 (SAS)\n平均得分: 21.2\n平均籃板: 6.8\n平均助攻: 2.6\n投籃命中率: 50.6%\n三分命中率: 44.3%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2016-17 (SAS)", text="2016-17 (SAS)\n平均得分: 25.5\n平均籃板: 5.8\n平均助攻: 3.5\n投籃命中率: 48.5%\n三分命中率: 38.0%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2017-18 (SAS)", text="2017-18 (SAS)\n平均得分: 16.2\n平均籃板: 4.7\n平均助攻: 2.3\n投籃命中率: 46.8%\n三分命中率: 31.4%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2018-19 (TOR)", text="2018-19 (TOR)\n平均得分: 26.6\n平均籃板: 7.3\n平均助攻: 3.3\n投籃命中率: 49.6%\n三分命中率: 37.1%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2019-20 (LAC)", text="2019-20 (LAC)\n平均得分: 27.1\n平均籃板: 7.1\n平均助攻: 4.9\n投籃命中率: 47.0%\n三分命中率: 37.8%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2020-21 (LAC)", text="2020-21 (LAC)\n平均得分: 24.8\n平均籃板: 6.5\n平均助攻: 5.2\n投籃命中率: 51.2%\n三分命中率: 39.8%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2022-23 (LAC)", text="2022-23 (LAC)\n平均得分: 23.8\n平均籃板: 6.5\n平均助攻: 3.9\n投籃命中率: 51.2%\n三分命中率: 41.6%")
                        ),
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

#######################################################GiannisAntetokounmpo#####################################################################################
    if event.message.text == 'GiannisAntetokounmpo':
        try:
            message = TextSendMessage(
                text='請選擇2013-14~2022-23賽季',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="2013-14 (MIL)", text="2013-14 (MIL)\n平均得分: 6.8\n平均籃板: 4.4\n平均助攻: 1.9\n投籃命中率: 41.4%\n三分命中率: 34.7%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2014-15 (MIL)", text="2014-15 (MIL)\n平均得分: 12.7\n平均籃板: 6.7\n平均助攻: 2.6\n投籃命中率: 49.1%\n三分命中率: 15.9%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2015-16 (MIL)", text="2015-16 (MIL)\n平均得分: 16.9\n平均籃板: 7.7\n平均助攻: 4.3\n投籃命中率: 50.6%\n三分命中率: 25.7%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2016-17 (MIL)", text="2016-17 (MIL)\n平均得分: 22.9\n平均籃板: 8.8\n平均助攻: 5.4\n投籃命中率: 52.1%\n三分命中率: 27.2%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2017-18 (MIL)", text="2017-18 (MIL)\n平均得分: 26.9\n平均籃板: 10.0\n平均助攻: 4.8\n投籃命中率: 52.9%\n三分命中率: 30.7%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2018-19 (MIL)", text="2018-19 (MIL)\n平均得分: 27.7\n平均籃板: 12.5\n平均助攻: 5.9\n投籃命中率: 57.8%\n三分命中率: 25.6%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2019-20 (MIL)", text="2019-20 (MIL)\n平均得分: 29.5\n平均籃板: 13.6\n平均助攻: 5.6\n投籃命中率: 55.3%\n三分命中率: 30.4%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2020-21 (MIL)", text="2020-21 (MIL)\n平均得分: 28.1\n平均籃板: 11.0\n平均助攻: 5.9\n投籃命中率: 56.9%\n三分命中率: 30.3%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2021-22 (MIL)", text="2021-22 (MIL)\n平均得分: 29.9\n平均籃板: 11.7\n平均助攻: 5.4\n投籃命中率: 52.0%\n三分命中率: 19.3%")
                        ),
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

###########################################################StephenCurry#################################################################################
    if event.message.text == 'StephenCurry':
        try:
            message = TextSendMessage(
                text='請選擇賽季',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="-2009-10~2017-18賽季", text="-2009-10~2017-18賽季")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="-2018-19~2022-23賽季", text="-2018-19~2022-23賽季")
                        ),
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

    if event.message.text == '-2009-10~2017-18賽季':
        try:
            message = TextSendMessage(
                text='請選擇賽季',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="2009-10 (GSW)", text="2009-10 (GSW)\n平均得分: 17.5\n平均籃板: 4.5\n平均助攻: 5.9\n投籃命中率: 46.2%\n三分命中率: 43.7%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2010-11 (GSW)", text="2010-11 (GSW)\n平均得分: 18.6\n平均籃板: 3.9\n平均助攻: 5.8\n投籃命中率: 48.0%\n三分命中率: 44.2%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2011-12 (GSW)", text="2011-12 (GSW)\n平均得分: 14.7\n平均籃板: 3.4\n平均助攻: 5.3\n投籃命中率: 49.0%\n三分命中率: 45.5%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2012-13 (GSW)", text="2012-13 (GSW)\n平均得分: 22.9\n平均籃板: 4.0\n平均助攻: 6.9\n投籃命中率: 45.1%\n三分命中率: 45.3%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2013-14 (GSW)", text="2013-14 (GSW)\n平均得分: 24.0\n平均籃板: 4.3\n平均助攻: 8.5\n投籃命中率: 47.1%\n三分命中率: 42.4%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2014-15 (GSW)", text="2014-15 (GSW)\n平均得分: 23.8\n平均籃板: 4.3\n平均助攻: 7.7\n投籃命中率: 48.7%\n三分命中率: 44.3%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2015-16 (GSW)", text="2015-16 (GSW)\n平均得分: 30.1\n平均籃板: 5.4\n平均助攻: 6.7\n投籃命中率: 50.4%\n三分命中率: 45.4%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2016-17 (GSW)", text="2016-17 (GSW)\n平均得分: 25.3\n平均籃板: 4.5\n平均助攻: 6.6\n投籃命中率: 46.8%\n三分命中率: 41.1%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2017-18 (GSW)", text="2017-18 (GSW)\n平均得分: 26.4\n平均籃板: 5.1\n平均助攻: 6.1\n投籃命中率: 49.5%\n三分命中率: 42.3%")
                        ),
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
    if event.message.text == '-2018-19~2022-23賽季':
        try:
            message = TextSendMessage(
                text='請選擇賽季',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="2018-19 (GSW)", text="2018-19 (GSW)\n平均得分: 27.3\n平均籃板: 5.3\n平均助攻: 5.2\n投籃命中率: 47.2%\n三分命中率: 43.7%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2019-20 (GSW)", text="2019-20 (GSW)\n平均得分: 20.8\n平均籃板: 5.2\n平均助攻: 6.6\n投籃命中率: 40.2%\n三分命中率: 24.5%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2020-21 (GSW)", text="2020-21 (GSW)\n平均得分: 32.0\n平均籃板: 5.5\n平均助攻: 5.8\n投籃命中率: 48.2%\n三分命中率: 42.1%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2021-22 (GSW)", text="2021-22 (GSW)\n平均得分: 25.5\n平均籃板: 5.2\n平均助攻: 6.3\n投籃命中率: 43.7%\n三分命中率: 38.0%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2022-23 (GSW)", text="2022-23 (GSW)\n平均得分: 29.4\n平均籃板: 6.1\n平均助攻: 6.3\n投籃命中率: 49.3%\n三分命中率: 42.7%")
                        ),
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
##############################################################AnthonyDavis##############################################################################
    if event.message.text == 'AnthonyDavis':
        try:
            message = TextSendMessage(
                text='請選擇賽季',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="AnthonyDavis2012-13~2017-18賽季", text="AnthonyDavis2012-13~2017-18賽季")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="AnthonyDavis2018-19~2022-23賽季", text="AnthonyDavis2018-19~2022-23賽季")
                        ),
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

    if event.message.text == 'AnthonyDavis2012-13~2017-18賽季':
        try:
            message = TextSendMessage(
                text='請選擇賽季',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="2012-13 (NOH)", text="2012-13 (NOH)\n平均得分: 13.5\n平均籃板: 8.2\n平均助攻: 1.0\n投籃命中率: 51.6%\n三分命中率: 0.0%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2013-14 (NOP)", text="2013-14 (NOP)\n平均得分: 20.8\n平均籃板: 10.0\n平均助攻: 1.6\n投籃命中率: 51.9%\n三分命中率: 22.2%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2014-15 (NOP)", text="2014-15 (NOP)\n平均得分: 24.4\n平均籃板: 10.2\n平均助攻: 2.2\n投籃命中率: 53.5%\n三分命中率: 8.3%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2015-16 (NOP)", text="2015-16 (NOP)\n平均得分: 24.3\n平均籃板: 10.3\n平均助攻: 1.9\n投籃命中率: 49.3%\n三分命中率: 32.4%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2016-17 (NOP)", text="2016-17 (NOP)\n平均得分: 28.0\n平均籃板: 11.8\n平均助攻: 2.1\n投籃命中率: 50.5%\n三分命中率: 29.9%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2017-18 (NOP)", text="2017-18 (NOP)\n平均得分: 28.1\n平均籃板: 11.1\n平均助攻: 2.3\n投籃命中率: 53.4%\n三分命中率: 34.0%")
                        ),
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
    if event.message.text == 'AnthonyDavis2018-19~2022-23賽季':
        try:
            message = TextSendMessage(
                text='請選擇賽季',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="2018-19 (NOP)", text="2018-19 (NOP)\n平均得分: 25.9\n平均籃板: 12.0\n平均助攻: 3.9\n投籃命中率: 51.7%\n三分命中率: 33.1%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2019-20 (LAL)", text="2019-20 (LAL)\n平均得分: 26.1\n平均籃板: 9.3\n平均助攻: 3.2\n投籃命中率: 50.3%\n三分命中率: 33.0%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2020-21 (LAL)", text="2020-21 (LAL)\n平均得分: 21.8\n平均籃板: 7.9\n平均助攻: 3.1\n投籃命中率: 49.1%\n三分命中率: 26.0%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2021-22 (LAL)", text="2021-22 (LAL)\n平均得分: 23.2\n平均籃板: 9.9\n平均助攻: 3.1\n投籃命中率: 53.2%\n三分命中率: 18.6%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2022-23 (LAL)", text="2022-23 (LAL)\n平均得分: 25.9\n平均籃板: 12.5\n平均助攻: 2.6\n投籃命中率: 56.3%\n三分命中率: 25.7%")
                        ),
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
#################################################################JoelEmbiid###############################################################################################
    if event.message.text == 'JoelEmbiid':
        try:
            message = TextSendMessage(
                text='請選擇2016-17~2022-23賽季',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="2016-17 (PHI)", text="2016-17 (PHI)\n平均得分: 20.2\n平均籃板: 7.8\n平均助攻: 2.1\n投籃命中率: 46.6%\n三分命中率: 36.7%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2017-18 (PHI)", text="2017-18 (PHI)\n平均得分: 22.9\n平均籃板: 11.0\n平均助攻: 3.2\n投籃命中率: 48.3%\n三分命中率: 30.8%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2018-19 (PHI)", text="2018-19 (PHI)\n平均得分: 27.5\n平均籃板: 13.6\n平均助攻: 3.7\n投籃命中率: 48.4%\n三分命中率: 30.0%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2019-20 (PHI)", text="2019-20 (PHI)\n平均得分: 23.0\n平均籃板: 11.6\n平均助攻: 3.0\n投籃命中率: 47.7%\n三分命中率: 33.1%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2020-21 (PHI)", text="2020-21 (PHI)\n平均得分: 28.5\n平均籃板: 10.6\n平均助攻: 2.8\n投籃命中率: 51.3%\n三分命中率: 37.7%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2021-22 (PHI)", text="2021-22 (PHI)\n平均得分: 30.6\n平均籃板: 11.7\n平均助攻: 4.2\n投籃命中率: 49.9%\n三分命中率: 37.1%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2022-23 (PHI)", text="2022-23 (PHI)\n平均得分: 33.1\n平均籃板: 10.2\n平均助攻: 4.2\n投籃命中率: 54.8%\n三分命中率: 33.0%")
                        ),
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

##################################################################NikolaJokic##############################################################################################
    if event.message.text == 'NikolaJokic':
        try:
            message = TextSendMessage(
                text='請選擇2015-16~2022-23賽季',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="2015-16 (DEN)", text="2015-16 (DEN)\n平均得分: 10.0\n平均籃板: 7.0\n平均助攻: 2.4\n投籃命中率: 51.2%\n三分命中率: 33.3%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2016-17 (DEN)", text="2016-17 (DEN)\n平均得分: 16.7\n平均籃板: 9.8\n平均助攻: 4.9\n投籃命中率: 57.8%\n三分命中率: 32.4%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2017-18 (DEN)", text="2017-18 (DEN)\n平均得分: 18.5\n平均籃板: 10.7\n平均助攻: 6.1\n投籃命中率: 49.9%\n三分命中率: 39.6%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2018-19 (DEN)", text="2018-19 (DEN)\n平均得分: 20.1\n平均籃板: 10.8\n平均助攻: 7.3\n投籃命中率: 51.1%\n三分命中率: 30.7%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2019-20 (DEN)", text="2019-20 (DEN)\n平均得分: 19.9\n平均籃板: 9.7\n平均助攻: 7.0\n投籃命中率: 52.8%\n三分命中率: 31.4%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2020-21 (DEN)", text="2020-21 (DEN)\n平均得分: 26.4\n平均籃板: 10.8\n平均助攻: 8.3\n投籃命中率: 56.6%\n三分命中率: 38.8%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2021-22 (DEN)", text="2021-22 (DEN)\n平均得分: 27.1\n平均籃板: 13.8\n平均助攻: 7.9\n投籃命中率: 58.3%\n三分命中率: 33.7%")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="2022-23 (DEN)", text="2022-23 (DEN)\n平均得分: 24.5\n平均籃板: 11.8\n平均助攻: 9.8\n投籃命中率: 63.2%\n三分命中率: 38.3%")
                        ),
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))   

    ####################
    # bert啟動器#########
    text = event.message.text
    text = bert([text])  # 文本分類函式
    print(text)
    ####################
    if text == "歡迎":  # 關鍵字錯誤
        a01 = ["歡迎使用NBA-BOT"]
        content_arr = []
        content_arr.append(TextSendMessage(random_statement(a01)))
        content_arr.append(TextSendMessage(random_statement(nba)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0
    
    
    if text == "球員數據":
        content_arr = []
        content_arr.append(FlexSendMessage('請選擇球隊', GetTeam()))
        line_bot_api.reply_message(event.reply_token, content_arr)
    
    # 處理 Postback 事件的邏輯
    @handler.add(PostbackEvent)
    def handle_postback(event):
        data = event.postback.data

        # 初始化 content_arr
        content_arr = []

        if data.startswith('SelectPlayerFrom'):
           # 取得球隊名稱，這裡假設你的格式是 'SelectPlayerFrom TeamA'
           team = data.split(' ')[1]  # 使用明確的分隔符，避免出錯
           content_arr.append(FlexSendMessage('請選擇球員', GetTeamAllPlayers(team)))
           line_bot_api.reply_message(event.reply_token, content_arr)

        elif data.startswith('SelectPlayerName'):
            # 取得球員名稱，這裡假設你的格式是 'SelectPlayerName PlayerName'
            name = data.split(' ')[1]
            content_arr.append(FlexSendMessage('查詢結果出爐~', GetPlayer(name)))
            line_bot_api.reply_message(event.reply_token, content_arr)


    if text == "今日賽事":
        content_arr = []
        games_info = get_nba_games_info()
        content_arr.append(TextSendMessage(games_info))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "過去賽事":  # 搜尋過去賽事時必須加上日期，例如:20220613
        # 使用正則表達式提取日期
        match = re.search(r"(\d{8})", event.message.text)
        if match:
            date = match.group(1)
            games = get_games(date)
            content_arr = [
                TextSendMessage("\n".join(games) if games else f"{date} 無賽事。")
            ]
        else:
            content_arr = [TextSendMessage("因時間設定為美國\n須往前一天做詢問\n請提供正確的日期格式\n例如:過去賽事20240102。")]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "巫師陣容":
        team_code = "wizards"
        roster_data = GetTeamRoster(team_code)
        content_arr = []
        if roster_data is not None:
            roster_text = "\n".join(
                [
                    f"{player['displayName']} ({player['position']}): 身高 {player['height']}, 體重 {player['weight']}"
                    for player in roster_data
                ]
            )
            content_arr.append(TextSendMessage(text=roster_text))
        else:
            content_arr.append(TextSendMessage(text="無法取得陣容數據"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "黃蜂陣容":
        team_code = "hornets"
        roster_data = GetTeamRoster(team_code)
        content_arr = []
        if roster_data is not None:
            roster_text = "\n".join(
                [
                    f"{player['displayName']} ({player['position']}): 身高 {player['height']}, 體重 {player['weight']}"
                    for player in roster_data
                ]
            )
            content_arr.append(TextSendMessage(text=roster_text))
        else:
            content_arr.append(TextSendMessage(text="無法取得陣容數據"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "老鷹陣容":
        team_code = "hawks"
        roster_data = GetTeamRoster(team_code)
        content_arr = []
        if roster_data is not None:
            roster_text = "\n".join(
                [
                    f"{player['displayName']} ({player['position']}): 身高 {player['height']}, 體重 {player['weight']}"
                    for player in roster_data
                ]
            )
            content_arr.append(TextSendMessage(text=roster_text))
        else:
            content_arr.append(TextSendMessage(text="無法取得陣容數據"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "熱火陣容":
        team_code = "heat"
        roster_data = GetTeamRoster(team_code)
        content_arr = []
        if roster_data is not None:
            roster_text = "\n".join(
                [
                    f"{player['displayName']} ({player['position']}): 身高 {player['height']}, 體重 {player['weight']}"
                    for player in roster_data
                ]
            )
            content_arr.append(TextSendMessage(text=roster_text))
        else:
            content_arr.append(TextSendMessage(text="無法取得陣容數據"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "魔術陣容":
        team_code = "magic"
        roster_data = GetTeamRoster(team_code)
        content_arr = []
        if roster_data is not None:
            roster_text = "\n".join(
                [
                    f"{player['displayName']} ({player['position']}): 身高 {player['height']}, 體重 {player['weight']}"
                    for player in roster_data
                ]
            )
            content_arr.append(TextSendMessage(text=roster_text))
        else:
            content_arr.append(TextSendMessage(text="無法取得陣容數據"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "尼克陣容":
        team_code = "knicks"
        roster_data = GetTeamRoster(team_code)
        content_arr = []
        if roster_data is not None:
            roster_text = "\n".join(
                [
                    f"{player['displayName']} ({player['position']}): 身高 {player['height']}, 體重 {player['weight']}"
                    for player in roster_data
                ]
            )
            content_arr.append(TextSendMessage(text=roster_text))
        else:
            content_arr.append(TextSendMessage(text="無法取得陣容數據"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "76人陣容":
        team_code = "76ers"
        roster_data = GetTeamRoster(team_code)
        content_arr = []
        if roster_data is not None:
            roster_text = "\n".join(
                [
                    f"{player['displayName']} ({player['position']}): 身高 {player['height']}, 體重 {player['weight']}"
                    for player in roster_data
                ]
            )
            content_arr.append(TextSendMessage(text=roster_text))
        else:
            content_arr.append(TextSendMessage(text="無法取得陣容數據"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "七六人陣容":
        team_code = "76ers"
        roster_data = GetTeamRoster(team_code)
        content_arr = []
        if roster_data is not None:
            roster_text = "\n".join(
                [
                    f"{player['displayName']} ({player['position']}): 身高 {player['height']}, 體重 {player['weight']}"
                    for player in roster_data
                ]
            )
            content_arr.append(TextSendMessage(text=roster_text))
        else:
            content_arr.append(TextSendMessage(text="無法取得陣容數據"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "籃網陣容":
        team_code = "nets"
        roster_data = GetTeamRoster(team_code)
        content_arr = []
        if roster_data is not None:
            roster_text = "\n".join(
                [
                    f"{player['displayName']} ({player['position']}): 身高 {player['height']}, 體重 {player['weight']}"
                    for player in roster_data
                ]
            )
            content_arr.append(TextSendMessage(text=roster_text))
        else:
            content_arr.append(TextSendMessage(text="無法取得陣容數據"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "塞爾提克陣容":
        team_code = "celtics"
        roster_data = GetTeamRoster(team_code)
        content_arr = []
        if roster_data is not None:
            roster_text = "\n".join(
                [
                    f"{player['displayName']} ({player['position']}): 身高 {player['height']}, 體重 {player['weight']}"
                    for player in roster_data
                ]
            )
            content_arr.append(TextSendMessage(text=roster_text))
        else:
            content_arr.append(TextSendMessage(text="無法取得陣容數據"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "暴龍陣容":
        team_code = "raptors"
        roster_data = GetTeamRoster(team_code)
        content_arr = []
        if roster_data is not None:
            roster_text = "\n".join(
                [
                    f"{player['displayName']} ({player['position']}): 身高 {player['height']}, 體重 {player['weight']}"
                    for player in roster_data
                ]
            )
            content_arr.append(TextSendMessage(text=roster_text))
        else:
            content_arr.append(TextSendMessage(text="無法取得陣容數據"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "公牛陣容":
        team_code = "bulls"
        roster_data = GetTeamRoster(team_code)
        content_arr = []
        if roster_data is not None:
            roster_text = "\n".join(
                [
                    f"{player['displayName']} ({player['position']}): 身高 {player['height']}, 體重 {player['weight']}"
                    for player in roster_data
                ]
            )
            content_arr.append(TextSendMessage(text=roster_text))
        else:
            content_arr.append(TextSendMessage(text="無法取得陣容數據"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "騎士陣容":
        team_code = "cavaliers"
        roster_data = GetTeamRoster(team_code)
        content_arr = []
        if roster_data is not None:
            roster_text = "\n".join(
                [
                    f"{player['displayName']} ({player['position']}): 身高 {player['height']}, 體重 {player['weight']}"
                    for player in roster_data
                ]
            )
            content_arr.append(TextSendMessage(text=roster_text))
        else:
            content_arr.append(TextSendMessage(text="無法取得陣容數據"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "溜馬陣容":
        team_code = "pacers"
        roster_data = GetTeamRoster(team_code)
        content_arr = []
        if roster_data is not None:
            roster_text = "\n".join(
                [
                    f"{player['displayName']} ({player['position']}): 身高 {player['height']}, 體重 {player['weight']}"
                    for player in roster_data
                ]
            )
            content_arr.append(TextSendMessage(text=roster_text))
        else:
            content_arr.append(TextSendMessage(text="無法取得陣容數據"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "活塞陣容":
        team_code = "pistons"
        roster_data = GetTeamRoster(team_code)
        content_arr = []
        if roster_data is not None:
            roster_text = "\n".join(
                [
                    f"{player['displayName']} ({player['position']}): 身高 {player['height']}, 體重 {player['weight']}"
                    for player in roster_data
                ]
            )
            content_arr.append(TextSendMessage(text=roster_text))
        else:
            content_arr.append(TextSendMessage(text="無法取得陣容數據"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "公鹿陣容":
        team_code = "bucks"
        roster_data = GetTeamRoster(team_code)
        content_arr = []
        if roster_data is not None:
            roster_text = "\n".join(
                [
                    f"{player['displayName']} ({player['position']}): 身高 {player['height']}, 體重 {player['weight']}"
                    for player in roster_data
                ]
            )
            content_arr.append(TextSendMessage(text=roster_text))
        else:
            content_arr.append(TextSendMessage(text="無法取得陣容數據"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "灰狼陣容":
        team_code = "timberwolves"
        roster_data = GetTeamRoster(team_code)
        content_arr = []
        if roster_data is not None:
            roster_text = "\n".join(
                [
                    f"{player['displayName']} ({player['position']}): 身高 {player['height']}, 體重 {player['weight']}"
                    for player in roster_data
                ]
            )
            content_arr.append(TextSendMessage(text=roster_text))
        else:
            content_arr.append(TextSendMessage(text="無法取得陣容數據"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "爵士陣容":
        team_code = "jazz"
        roster_data = GetTeamRoster(team_code)
        content_arr = []
        if roster_data is not None:
            roster_text = "\n".join(
                [
                    f"{player['displayName']} ({player['position']}): 身高 {player['height']}, 體重 {player['weight']}"
                    for player in roster_data
                ]
            )
            content_arr.append(TextSendMessage(text=roster_text))
        else:
            content_arr.append(TextSendMessage(text="無法取得陣容數據"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "雷霆陣容":
        team_code = "thunder"
        roster_data = GetTeamRoster(team_code)
        content_arr = []
        if roster_data is not None:
            roster_text = "\n".join(
                [
                    f"{player['displayName']} ({player['position']}): 身高 {player['height']}, 體重 {player['weight']}"
                    for player in roster_data
                ]
            )
            content_arr.append(TextSendMessage(text=roster_text))
        else:
            content_arr.append(TextSendMessage(text="無法取得陣容數據"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "拓荒者陣容":
        team_code = "blazers"
        roster_data = GetTeamRoster(team_code)
        content_arr = []
        if roster_data is not None:
            roster_text = "\n".join(
                [
                    f"{player['displayName']} ({player['position']}): 身高 {player['height']}, 體重 {player['weight']}"
                    for player in roster_data
                ]
            )
            content_arr.append(TextSendMessage(text=roster_text))
        else:
            content_arr.append(TextSendMessage(text="無法取得陣容數據"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "金塊陣容":
        team_code = "nuggets"
        roster_data = GetTeamRoster(team_code)
        content_arr = []
        if roster_data is not None:
            roster_text = "\n".join(
                [
                    f"{player['displayName']} ({player['position']}): 身高 {player['height']}, 體重 {player['weight']}"
                    for player in roster_data
                ]
            )
            content_arr.append(TextSendMessage(text=roster_text))
        else:
            content_arr.append(TextSendMessage(text="無法取得陣容數據"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "灰熊陣容":
        team_code = "grizzlies"
        roster_data = GetTeamRoster(team_code)
        content_arr = []
        if roster_data is not None:
            roster_text = "\n".join(
                [
                    f"{player['displayName']} ({player['position']}): 身高 {player['height']}, 體重 {player['weight']}"
                    for player in roster_data
                ]
            )
            content_arr.append(TextSendMessage(text=roster_text))
        else:
            content_arr.append(TextSendMessage(text="無法取得陣容數據"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "火箭陣容":
        team_code = "rockets"
        roster_data = GetTeamRoster(team_code)
        content_arr = []
        if roster_data is not None:
            roster_text = "\n".join(
                [
                    f"{player['displayName']} ({player['position']}): 身高 {player['height']}, 體重 {player['weight']}"
                    for player in roster_data
                ]
            )
            content_arr.append(TextSendMessage(text=roster_text))
        else:
            content_arr.append(TextSendMessage(text="無法取得陣容數據"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "鵜鶘教練":
        team_code = "pelicans"
        roster_data = GetTeamRoster(team_code)
        content_arr = []
        if roster_data is not None:
            roster_text = "\n".join(
                [
                    f"{player['displayName']} ({player['position']}): 身高 {player['height']}, 體重 {player['weight']}"
                    for player in roster_data
                ]
            )
            content_arr.append(TextSendMessage(text=roster_text))
        else:
            content_arr.append(TextSendMessage(text="無法取得陣容數據"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "馬刺陣容":
        team_code = "spurs"
        roster_data = GetTeamRoster(team_code)
        content_arr = []
        if roster_data is not None:
            roster_text = "\n".join(
                [
                    f"{player['displayName']} ({player['position']}): 身高 {player['height']}, 體重 {player['weight']}"
                    for player in roster_data
                ]
            )
            content_arr.append(TextSendMessage(text=roster_text))
        else:
            content_arr.append(TextSendMessage(text="無法取得陣容數據"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "獨行俠陣容":
        team_code = "mavericks"
        roster_data = GetTeamRoster(team_code)
        content_arr = []
        if roster_data is not None:
            roster_text = "\n".join(
                [
                    f"{player['displayName']} ({player['position']}): 身高 {player['height']}, 體重 {player['weight']}"
                    for player in roster_data
                ]
            )
            content_arr.append(TextSendMessage(text=roster_text))
        else:
            content_arr.append(TextSendMessage(text="無法取得陣容數據"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "勇士陣容":
        team_code = "warriors"
        roster_data = GetTeamRoster(team_code)
        content_arr = []
        if roster_data is not None:
            roster_text = "\n".join(
                [
                    f"{player['displayName']} ({player['position']}): 身高 {player['height']}, 體重 {player['weight']}"
                    for player in roster_data
                ]
            )
            content_arr.append(TextSendMessage(text=roster_text))
        else:
            content_arr.append(TextSendMessage(text="無法取得陣容數據"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "湖人陣容":
        team_code = "lakers"
        roster_data = GetTeamRoster(team_code)
        content_arr = []
        if roster_data is not None:
            roster_text = "\n".join(
                [
                    f"{player['displayName']} ({player['position']}): 身高 {player['height']}, 體重 {player['weight']}"
                    for player in roster_data
                ]
            )
            content_arr.append(TextSendMessage(text=roster_text))
        else:
            content_arr.append(TextSendMessage(text="無法取得陣容數據"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "快艇陣容":
        team_code = "clippers"
        roster_data = GetTeamRoster(team_code)
        content_arr = []
        if roster_data is not None:
            roster_text = "\n".join(
                [
                    f"{player['displayName']} ({player['position']}): 身高 {player['height']}, 體重 {player['weight']}"
                    for player in roster_data
                ]
            )
            content_arr.append(TextSendMessage(text=roster_text))
        else:
            content_arr.append(TextSendMessage(text="無法取得陣容數據"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "太陽陣容":
        team_code = "suns"
        roster_data = GetTeamRoster(team_code)
        content_arr = []
        if roster_data is not None:
            roster_text = "\n".join(
                [
                    f"{player['displayName']} ({player['position']}): 身高 {player['height']}, 體重 {player['weight']}"
                    for player in roster_data
                ]
            )
            content_arr.append(TextSendMessage(text=roster_text))
        else:
            content_arr.append(TextSendMessage(text="無法取得陣容數據"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "國王陣容":
        team_code = "kings"
        roster_data = GetTeamRoster(team_code)
        content_arr = []
        if roster_data is not None:
            roster_text = "\n".join(
                [
                    f"{player['displayName']} ({player['position']}): 身高 {player['height']}, 體重 {player['weight']}"
                    for player in roster_data
                ]
            )
            content_arr.append(TextSendMessage(text=roster_text))
        else:
            content_arr.append(TextSendMessage(text="無法取得陣容數據"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "MVP":
        content_arr = []
        content_arr.append(TextSendMessage(random_statement(MVP)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "新人王":
        content_arr = []
        content_arr.append(TextSendMessage(random_statement(新人王)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "最佳進步獎":
        content_arr = []
        content_arr.append(TextSendMessage(random_statement(最佳進步獎)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "最佳教練":
        content_arr = []
        content_arr.append(TextSendMessage(random_statement(最佳教練)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "最佳第六人":
        content_arr = []
        content_arr.append(TextSendMessage(random_statement(最佳第六人)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0
    
    if text == "最佳第6人":
        content_arr = []
        content_arr.append(TextSendMessage(random_statement(最佳第6人)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "年度獎項":
        content_arr = []
        content_arr.append(TextSendMessage(random_statement(年度獎項)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "最佳防守球員":
        content_arr = []
        content_arr.append(TextSendMessage(random_statement(最佳防守球員)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0
    
    if text == "年度第一隊":
        content_arr = []
        content_arr.append(TextSendMessage(random_statement(年度第一隊)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "年度第1隊":
        content_arr = []
        content_arr.append(TextSendMessage(random_statement(年度第1隊)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0
    
    if text == "年度第二隊":
        content_arr = []
        content_arr.append(TextSendMessage(random_statement(年度第二隊)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0
    
    if text == "年度第2隊":
        content_arr = []
        content_arr.append(TextSendMessage(random_statement(年度第2隊)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "年度第三隊":
        content_arr = []
        content_arr.append(TextSendMessage(random_statement(年度第三隊)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0
    
    if text == "年度第3隊":
        content_arr = []
        content_arr.append(TextSendMessage(random_statement(年度第3隊)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你選秀資料"))
        content_arr.append(TextSendMessage(GetAllDraftInfo()))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第一順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第一順位"))
        content_arr.append(TextSendMessage(random_statement(第一順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第1順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第1順位"))
        content_arr.append(TextSendMessage(random_statement(第一順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "狀元":
        content_arr = []
        content_arr.append(TextSendMessage("提供你狀元"))
        content_arr.append(TextSendMessage(random_statement(第一順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第二順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第二順位"))
        content_arr.append(TextSendMessage(random_statement(第二順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第2順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第2順位"))
        content_arr.append(TextSendMessage(random_statement(第二順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "榜眼":
        content_arr = []
        content_arr.append(TextSendMessage("提供你榜眼"))
        content_arr.append(TextSendMessage(random_statement(第二順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第三順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第三順位"))
        content_arr.append(TextSendMessage(random_statement(第三順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第3順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第3順位"))
        content_arr.append(TextSendMessage(random_statement(第三順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "探花":
        content_arr = []
        content_arr.append(TextSendMessage("提供你探花"))
        content_arr.append(TextSendMessage(random_statement(第三順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第四順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第四順位"))
        content_arr.append(TextSendMessage(random_statement(第四順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第4順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第4順位"))
        content_arr.append(TextSendMessage(random_statement(第四順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第五順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第五順位"))
        content_arr.append(TextSendMessage(random_statement(第五順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第5順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第5順位"))
        content_arr.append(TextSendMessage(random_statement(第五順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第六順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第六順位"))
        content_arr.append(TextSendMessage(random_statement(第六順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第6順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第6順位"))
        content_arr.append(TextSendMessage(random_statement(第六順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第七順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第七順位"))
        content_arr.append(TextSendMessage(random_statement(第七順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第7順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第7順位"))
        content_arr.append(TextSendMessage(random_statement(第七順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第八順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第八順位"))
        content_arr.append(TextSendMessage(random_statement(第八順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第8順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第8順位"))
        content_arr.append(TextSendMessage(random_statement(第八順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第九順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第九順位"))
        content_arr.append(TextSendMessage(random_statement(第九順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第9順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第9順位"))
        content_arr.append(TextSendMessage(random_statement(第九順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第十順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第十順位"))
        content_arr.append(TextSendMessage(random_statement(第十順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第10順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第10順位"))
        content_arr.append(TextSendMessage(random_statement(第十順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第十一順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第十一順位"))
        content_arr.append(TextSendMessage(random_statement(第十一順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第11順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第11順位"))
        content_arr.append(TextSendMessage(random_statement(第十一順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第十二順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第十二順位"))
        content_arr.append(TextSendMessage(random_statement(第十二順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第12順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第12順位"))
        content_arr.append(TextSendMessage(random_statement(第十二順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第十三順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第十三順位"))
        content_arr.append(TextSendMessage(random_statement(第十三順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第13順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第13順位"))
        content_arr.append(TextSendMessage(random_statement(第十三順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第十四順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第十四順位"))
        content_arr.append(TextSendMessage(random_statement(第十四順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第14順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第14順位"))
        content_arr.append(TextSendMessage(random_statement(第十四順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第十五順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第十五順位"))
        content_arr.append(TextSendMessage(random_statement(第十五順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第15順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第15順位"))
        content_arr.append(TextSendMessage(random_statement(第十五順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第十六順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第十六順位"))
        content_arr.append(TextSendMessage(random_statement(第十六順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第16順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第16順位"))
        content_arr.append(TextSendMessage(random_statement(第十六順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第十七順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第十七順位"))
        content_arr.append(TextSendMessage(random_statement(第十七順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第17順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第17順位"))
        content_arr.append(TextSendMessage(random_statement(第十七順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第十八順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第十八順位"))
        content_arr.append(TextSendMessage(random_statement(第十八順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第18順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第18順位"))
        content_arr.append(TextSendMessage(random_statement(第十八順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第十九順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第十九順位"))
        content_arr.append(TextSendMessage(random_statement(第十九順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第19順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第19順位"))
        content_arr.append(TextSendMessage(random_statement(第十九順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第二十順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第二十順位"))
        content_arr.append(TextSendMessage(random_statement(第二十順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第20順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第20順位"))
        content_arr.append(TextSendMessage(random_statement(第二十順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第二十一順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第二十一順位"))
        content_arr.append(TextSendMessage(random_statement(第二十一順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第21順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第21順位"))
        content_arr.append(TextSendMessage(random_statement(第二十一順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第二十二順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第二十二順位"))
        content_arr.append(TextSendMessage(random_statement(第二十二順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第22順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第22順位"))
        content_arr.append(TextSendMessage(random_statement(第二十二順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第二十三順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第二十三順位"))
        content_arr.append(TextSendMessage(random_statement(第二十三順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第23順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第23順位"))
        content_arr.append(TextSendMessage(random_statement(第二十三順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第二十四順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第二十四順位"))
        content_arr.append(TextSendMessage(random_statement(第二十四順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第24順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第24順位"))
        content_arr.append(TextSendMessage(random_statement(第二十四順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第二十五順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第二十五順位"))
        content_arr.append(TextSendMessage(random_statement(第二十五順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第25順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第25順位"))
        content_arr.append(TextSendMessage(random_statement(第二十五順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第二十六順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第二十六順位"))
        content_arr.append(TextSendMessage(random_statement(第二十六順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第26順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第26順位"))
        content_arr.append(TextSendMessage(random_statement(第二十六順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第二十七順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第二十七順位"))
        content_arr.append(TextSendMessage(random_statement(第二十七順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第27順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第27順位"))
        content_arr.append(TextSendMessage(random_statement(第二十七順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第二十八順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第二十八順位"))
        content_arr.append(TextSendMessage(random_statement(第二十八順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第28順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第28順位"))
        content_arr.append(TextSendMessage(random_statement(第二十八順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第二十九順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第二十九順位"))
        content_arr.append(TextSendMessage(random_statement(第二十九順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第29順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第29順位"))
        content_arr.append(TextSendMessage(random_statement(第二十九順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第三十順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第三十順位"))
        content_arr.append(TextSendMessage(random_statement(第三十順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第30順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第30順位"))
        content_arr.append(TextSendMessage(random_statement(第三十順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第三十一順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第三十一順位"))
        content_arr.append(TextSendMessage(random_statement(第三十一順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第31順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第31順位"))
        content_arr.append(TextSendMessage(random_statement(第三十一順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第三十二順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第三十二順位"))
        content_arr.append(TextSendMessage(random_statement(第三十二順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第32順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第32順位"))
        content_arr.append(TextSendMessage(random_statement(第三十二順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第三十三順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第三十三順位"))
        content_arr.append(TextSendMessage(random_statement(第三十三順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第33順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第33順位"))
        content_arr.append(TextSendMessage(random_statement(第三十三順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第三十四順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第三十四順位"))
        content_arr.append(TextSendMessage(random_statement(第三十四順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第34順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第34順位"))
        content_arr.append(TextSendMessage(random_statement(第三十四順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第三十五順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第三十五順位"))
        content_arr.append(TextSendMessage(random_statement(第三十五順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第35順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第35順位"))
        content_arr.append(TextSendMessage(random_statement(第三十五順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第三十六順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第三十六順位"))
        content_arr.append(TextSendMessage(random_statement(第三十六順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第36順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第36順位"))
        content_arr.append(TextSendMessage(random_statement(第三十六順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第三十七順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第三十七順位"))
        content_arr.append(TextSendMessage(random_statement(第三十七順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第37順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第37順位"))
        content_arr.append(TextSendMessage(random_statement(第三十七順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第三十八順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第三十八順位"))
        content_arr.append(TextSendMessage(random_statement(第三十八順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第38順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第38順位"))
        content_arr.append(TextSendMessage(random_statement(第三十八順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第三十九順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第三十九順位"))
        content_arr.append(TextSendMessage(random_statement(第三十九順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第39順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第39順位"))
        content_arr.append(TextSendMessage(random_statement(第三十九順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第四十順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第四十順位"))
        content_arr.append(TextSendMessage(random_statement(第四十順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第40順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第40順位"))
        content_arr.append(TextSendMessage(random_statement(第四十順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第四十一順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第四十一順位"))
        content_arr.append(TextSendMessage(random_statement(第四十一順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第41順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第41順位"))
        content_arr.append(TextSendMessage(random_statement(第四十一順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第四十二順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第四十二順位"))
        content_arr.append(TextSendMessage(random_statement(第四十二順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第42順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第42順位"))
        content_arr.append(TextSendMessage(random_statement(第四十二順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第四十三順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第四十三順位"))
        content_arr.append(TextSendMessage(random_statement(第四十三順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第43順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第43順位"))
        content_arr.append(TextSendMessage(random_statement(第四十三順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第四十四順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第四十四順位"))
        content_arr.append(TextSendMessage(random_statement(第四十四順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第44順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第44順位"))
        content_arr.append(TextSendMessage(random_statement(第四十四順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第四十五順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第四十五順位"))
        content_arr.append(TextSendMessage(random_statement(第四十五順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第45順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第45順位"))
        content_arr.append(TextSendMessage(random_statement(第四十五順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第四十六順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第四十六順位"))
        content_arr.append(TextSendMessage(random_statement(第四十六順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第46順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第46順位"))
        content_arr.append(TextSendMessage(random_statement(第四十六順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第四十七順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第四十七順位"))
        content_arr.append(TextSendMessage(random_statement(第四十七順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第47順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第47順位"))
        content_arr.append(TextSendMessage(random_statement(第四十七順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第四十八順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第四十八順位"))
        content_arr.append(TextSendMessage(random_statement(第四十八順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第48順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第48順位"))
        content_arr.append(TextSendMessage(random_statement(第四十八順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第四十九順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第四十九順位"))
        content_arr.append(TextSendMessage(random_statement(第四十九順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第49順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第49順位"))
        content_arr.append(TextSendMessage(random_statement(第四十九順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第五十順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第五十順位"))
        content_arr.append(TextSendMessage(random_statement(第五十順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第50順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第50順位"))
        content_arr.append(TextSendMessage(random_statement(第五十順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第五十一順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第五十一順位"))
        content_arr.append(TextSendMessage(random_statement(第五十一順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第51順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第51順位"))
        content_arr.append(TextSendMessage(random_statement(第五十一順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第五十二順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第五十二順位"))
        content_arr.append(TextSendMessage(random_statement(第五十二順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第52順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第52順位"))
        content_arr.append(TextSendMessage(random_statement(第五十二順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第五十三順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第五十三順位"))
        content_arr.append(TextSendMessage(random_statement(第五十三順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第53順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第53順位"))
        content_arr.append(TextSendMessage(random_statement(第五十三順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第五十四順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第五十四順位"))
        content_arr.append(TextSendMessage(random_statement(第五十四順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第54順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第54順位"))
        content_arr.append(TextSendMessage(random_statement(第五十四順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第五十五順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第五十五順位"))
        content_arr.append(TextSendMessage(random_statement(第五十五順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第55順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第55順位"))
        content_arr.append(TextSendMessage(random_statement(第五十五順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第五十六順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第五十六順位"))
        content_arr.append(TextSendMessage(random_statement(第五十六順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第56順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第56順位"))
        content_arr.append(TextSendMessage(random_statement(第五十六順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第五十七順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第五十七順位"))
        content_arr.append(TextSendMessage(random_statement(第五十七順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第57順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第57順位"))
        content_arr.append(TextSendMessage(random_statement(第五十七順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第五十八順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第五十八順位"))
        content_arr.append(TextSendMessage(random_statement(第五十八順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "第58順位選秀":
        content_arr = []
        content_arr.append(TextSendMessage("提供你第58順位"))
        content_arr.append(TextSendMessage(random_statement(第五十八順位選秀)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0



    if text == "交易市場":
        content_arr = []
        content_arr.append(TextSendMessage(FreeMarket()))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "排名":
        content_arr = []
        content_arr.append(TextSendMessage("以下提供給你所有球隊排名"))
        content_arr.append(TextSendMessage("需要各別搜尋請輸入\n球隊名稱加上排名"))
        content_arr.append(TextSendMessage("例如-勇士排名-"))
        content_arr.append(TextSendMessage(GetAllTeamStandings()))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "七六人排名":
        content_arr = []
        team_name = "七六人"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你七六人球隊排名"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "76人排名":
        content_arr = []
        team_name = "76人"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你76人球隊排名"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "公牛排名":
        content_arr = []
        team_name = "公牛"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你公牛球隊排名"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "公鹿排名":
        content_arr = []
        team_name = "公鹿"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你公鹿球隊排名"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "太陽排名":
        content_arr = []
        team_name = "太陽"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你太陽球隊排名"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "火箭排名":
        content_arr = []
        team_name = "火箭"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你火箭球隊排名"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "尼克排名":
        content_arr = []
        team_name = "尼克"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你尼克球隊排名"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "灰狼排名":
        content_arr = []
        team_name = "灰狼"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你灰狼球隊排名"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "灰熊排名":
        content_arr = []
        team_name = "灰熊"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你灰熊球隊排名"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "老鷹排名":
        content_arr = []
        team_name = "老鷹"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你老鷹球隊排名"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "巫師排名":
        content_arr = []
        team_name = "巫師"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你巫師球隊排名"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "快艇排名":
        content_arr = []
        team_name = "快艇"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你快艇球隊排名"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "拓荒者排名":
        content_arr = []
        team_name = "拓荒者"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你拓荒者球隊排名"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "金塊排名":
        content_arr = []
        team_name = "金塊"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你金塊球隊排名"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "勇士排名":
        content_arr = []
        team_name = "勇士"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你勇士球隊排名"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "活塞排名":
        content_arr = []
        team_name = "活塞"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你活塞球隊排名"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "馬刺排名":
        content_arr = []
        team_name = "馬刺"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你馬刺球隊排名"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "國王排名":
        content_arr = []
        team_name = "國王"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你國王球隊排名"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "湖人排名":
        content_arr = []
        team_name = "湖人"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你湖人球隊排名"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "黃蜂排名":
        content_arr = []
        team_name = "黃蜂"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你黃蜂球隊排名"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "塞爾提克排名":
        content_arr = []
        team_name = "塞爾提克"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你塞爾提克球隊排名"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "溜馬排名":
        content_arr = []
        team_name = "溜馬"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你溜馬球隊排名"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "雷霆排名":
        content_arr = []
        team_name = "雷霆"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你雷霆球隊排名"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "暴龍排名":
        content_arr = []
        team_name = "暴龍"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你暴龍球隊排名"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "熱火排名":
        content_arr = []
        team_name = "熱火"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你熱火球隊排名"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "獨行俠排名":
        content_arr = []
        team_name = "獨行俠"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你獨行俠球隊排名"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "爵士排名":
        content_arr = []
        team_name = "爵士"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你爵士球隊排名"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "騎士排名":
        content_arr = []
        team_name = "騎士"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你騎士球隊排名"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "鵜鶘排名":
        content_arr = []
        team_name = "鵜鶘"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你鵜鶘球隊排名"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "籃網排名":
        content_arr = []
        team_name = "籃網"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你籃網球隊排名"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "魔術排名":
        content_arr = []
        team_name = "魔術"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你魔術球隊排名"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "巫師教練":
        content_arr = []
        team_name = "巫師"
        coaches_info = WizardsCoach(html_wizards, team_name)
        if coaches_info:
            # 教練信息包括總教練、副教練、助理教練和訓練師
            head_coach = coaches_info["總教練"]
            assistant_coach = coaches_info["助理教練"]
            # 將球隊的教練信息轉換成文字格式
            coach_text = f"總教練: {team_name}隊 {head_coach}\n"
            coach_text += f'助理教練: {", ".join(assistant_coach)}\n'
            content_arr = [TextSendMessage(f"以下是{team_name}隊的教練團\n{coach_text}")]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "黃蜂教練":
        content_arr = []
        team_name = "黃蜂"
        coaches_info = HornetsCoach(html_hornets, team_name)
        if coaches_info:
            # 教練信息包括總教練、副教練、助理教練和訓練師
            head_coach = coaches_info["總教練"]
            assistant_coach = coaches_info["助理教練"]
            trainer = coaches_info["訓練師"]
            # 將球隊的教練信息轉換成文字格式
            coach_text = f"總教練: {team_name}隊 {head_coach}\n"
            coach_text += f'助理教練: {", ".join(assistant_coach)}\n'
            coach_text += f"訓練師: {', '.join(trainer)}\n"
            content_arr = [TextSendMessage(f"以下是{team_name}隊的教練團\n{coach_text}")]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "老鷹教練":
        content_arr = []
        team_name = "老鷹"
        coaches_info = HawksCoach(html_hawks, team_name)
        if coaches_info:
            # 教練信息包括總教練、副教練、助理教練和訓練師
            head_coach = coaches_info["總教練"]
            assistant_coach = coaches_info["助理教練"]
            trainer = coaches_info["訓練師"]
            # 將球隊的教練信息轉換成文字格式
            coach_text = f"總教練: {team_name}隊 {head_coach}\n"
            coach_text += f'助理教練: {", ".join(assistant_coach)}\n'
            coach_text += f"訓練師: {', '.join(trainer)}\n"
            content_arr = [TextSendMessage(f"以下是{team_name}隊的教練團\n{coach_text}")]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "熱火教練":
        content_arr = []
        team_name = "熱火"
        coaches_info = HeatCoach(html_heat, team_name)
        if coaches_info:
            # 教練信息包括總教練、副教練、助理教練和訓練師
            head_coach = coaches_info["總教練"]
            assistant_coach = coaches_info["助理教練"]
            trainer = coaches_info["訓練師"]
            # 將球隊的教練信息轉換成文字格式
            coach_text = f"總教練: {team_name}隊 {head_coach}\n"
            coach_text += f'助理教練: {", ".join(assistant_coach)}\n'
            coach_text += f"訓練師: {', '.join(trainer)}\n"
            content_arr = [TextSendMessage(f"以下是{team_name}隊的教練團\n{coach_text}")]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "魔術教練":
        content_arr = []
        team_name = "魔術"
        coaches_info = MagicCoach(html_magic, team_name)
        if coaches_info:
            # 教練信息包括總教練、副教練、助理教練和訓練師
            head_coach = coaches_info["總教練"]
            assistant_coach = coaches_info["助理教練"]
            trainer = coaches_info["訓練師"]
            # 將球隊的教練信息轉換成文字格式
            coach_text = f"總教練: {team_name}隊 {head_coach}\n"
            coach_text += f'助理教練: {", ".join(assistant_coach)}\n'
            coach_text += f"訓練師: {', '.join(trainer)}\n"
            content_arr = [TextSendMessage(f"以下是{team_name}隊的教練團\n{coach_text}")]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "尼克教練":
        content_arr = []
        team_name = "尼克"
        coaches_info = KnickCoach(html_knick, team_name)
        if coaches_info:
            # 教練信息包括總教練、副教練、助理教練和訓練師
            head_coach = coaches_info["總教練"]
            assistant_coaches = coaches_info["副教練"]
            assistant_coach = coaches_info["助理教練"]
            trainer = coaches_info["訓練師"]
            # 將球隊的教練信息轉換成文字格式
            coach_text = f"總教練: {team_name}隊 {head_coach}\n"
            coach_text += f'副教練: {", ".join(assistant_coaches)}\n'
            coach_text += f'助理教練: {", ".join(assistant_coach)}\n'
            coach_text += f"訓練師: {', '.join(trainer)}\n"
            content_arr = [TextSendMessage(f"以下是{team_name}隊的教練團\n{coach_text}")]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "七六人教練":
        content_arr = []
        team_name = "七六人"
        coaches_info = SixerCoach(html_sixer, team_name)
        if coaches_info:
            # 教練信息包括總教練、副教練、助理教練和訓練師
            head_coach = coaches_info["總教練"]
            assistant_coach = coaches_info["助理教練"]
            trainer = coaches_info["訓練師"]
            # 將球隊的教練信息轉換成文字格式
            coach_text = f"總教練: {team_name}隊 {head_coach}\n"
            coach_text += f'助理教練: {", ".join(assistant_coach)}\n'
            coach_text += f"訓練師: {', '.join(trainer)}\n"
            content_arr = [TextSendMessage(f"以下是{team_name}隊的教練團\n{coach_text}")]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "76人教練":
        content_arr = []
        team_name = "76人"
        coaches_info = SixerCoach(html_sixer, team_name)
        if coaches_info:
            # 教練信息包括總教練、副教練、助理教練和訓練師
            head_coach = coaches_info["總教練"]
            assistant_coach = coaches_info["助理教練"]
            trainer = coaches_info["訓練師"]
            # 將球隊的教練信息轉換成文字格式
            coach_text = f"總教練: {team_name}隊 {head_coach}\n"
            coach_text += f'助理教練: {", ".join(assistant_coach)}\n'
            coach_text += f"訓練師: {', '.join(trainer)}\n"
            content_arr = [TextSendMessage(f"以下是{team_name}隊的教練團\n{coach_text}")]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "籃網教練":
        content_arr = []
        team_name = "籃網"
        coaches_info = NetsCoach(html_nets, team_name)
        if coaches_info:
            # 教練信息包括總教練、副教練、助理教練和訓練師
            head_coach = coaches_info["總教練"]
            assistant_coach = coaches_info["助理教練"]
            # 將球隊的教練信息轉換成文字格式
            coach_text = f"總教練: {team_name}隊 {head_coach}\n"
            coach_text += f'助理教練: {", ".join(assistant_coach)}\n'
            content_arr = [TextSendMessage(f"以下是{team_name}隊的教練團\n{coach_text}")]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "塞爾提克教練":
        content_arr = []
        team_name = "塞爾提克"
        coaches_info = CelticsCoach(html_celtics, team_name)
        if coaches_info:
            # 教練信息包括總教練、副教練、助理教練和訓練師
            head_coach = coaches_info["總教練"]
            assistant_coach = coaches_info["助理教練"]
            trainer = coaches_info["訓練師"]
            # 將球隊的教練信息轉換成文字格式
            coach_text = f"總教練: {team_name}隊 {head_coach}\n"
            coach_text += f'助理教練: {", ".join(assistant_coach)}\n'
            coach_text += f"訓練師: {', '.join(trainer)}\n"
            content_arr = [TextSendMessage(f"以下是{team_name}隊的教練團\n{coach_text}")]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "暴龍教練":
        content_arr = []
        team_name = "暴龍"
        coaches_info = RaptorsCoach(html_raptors, team_name)
        if coaches_info:
            # 教練信息包括總教練、副教練、助理教練和訓練師
            head_coach = coaches_info["總教練"]
            assistant_coach = coaches_info["助理教練"]
            trainer = coaches_info["訓練師"]
            # 將球隊的教練信息轉換成文字格式
            coach_text = f"總教練: {team_name}隊 {head_coach}\n"
            coach_text += f'助理教練: {", ".join(assistant_coach)}\n'
            coach_text += f"訓練師: {', '.join(trainer)}\n"
            content_arr = [TextSendMessage(f"以下是{team_name}隊的教練團\n{coach_text}")]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "公牛教練":
        content_arr = []
        team_name = "公牛"
        coaches_info = BullsCoach(html_bulls, team_name)
        if coaches_info:
            # 教練信息包括總教練、副教練、助理教練和訓練師
            head_coach = coaches_info["總教練"]
            assistant_coach = coaches_info["助理教練"]
            trainer = coaches_info["訓練師"]
            # 將球隊的教練信息轉換成文字格式
            coach_text = f"總教練: {team_name}隊 {head_coach}\n"
            coach_text += f'助理教練: {", ".join(assistant_coach)}\n'
            coach_text += f"訓練師: {', '.join(trainer)}\n"
            content_arr = [TextSendMessage(f"以下是{team_name}隊的教練團\n{coach_text}")]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "騎士教練":
        content_arr = []
        team_name = "騎士"
        coaches_info = CavaliersCoach(html_cavaliers, team_name)
        if coaches_info:
            # 教練信息包括總教練、副教練、助理教練和訓練師
            head_coach = coaches_info["總教練"]
            assistant_coaches = coaches_info["副教練"]
            assistant_coach = coaches_info["助理教練"]
            trainer = coaches_info["訓練師"]
            # 將球隊的教練信息轉換成文字格式
            coach_text = f"總教練: {team_name}隊 {head_coach}\n"
            coach_text += f'副教練: {", ".join(assistant_coaches)}\n'
            coach_text += f'助理教練: {", ".join(assistant_coach)}\n'
            coach_text += f"訓練師: {', '.join(trainer)}\n"
            content_arr = [TextSendMessage(f"以下是{team_name}隊的教練團\n{coach_text}")]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "溜馬教練":
        content_arr = []
        team_name = "溜馬"
        coaches_info = PacersCoach(html_pacers, team_name)
        if coaches_info:
            # 教練信息包括總教練、副教練、助理教練和訓練師
            head_coach = coaches_info["總教練"]
            assistant_coaches = coaches_info["首席助理教練"]
            assistant_coach = coaches_info["助理教練"]
            trainer = coaches_info["訓練師"]
            # 將球隊的教練信息轉換成文字格式
            coach_text = f"總教練: {team_name}隊 {head_coach}\n"
            coach_text += f'首席助理教練: {", ".join(assistant_coaches)}\n'
            coach_text += f'助理教練: {", ".join(assistant_coach)}\n'
            coach_text += f"訓練師: {', '.join(trainer)}\n"
            content_arr = [TextSendMessage(f"以下是{team_name}隊的教練團\n{coach_text}")]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "活塞教練":
        content_arr = []
        team_name = "活塞"
        coaches_info = PistonsCoach(html_pistons, team_name)
        if coaches_info:
            # 教練信息包括總教練、副教練、助理教練和訓練師
            head_coach = coaches_info["總教練"]
            assistant_coach = coaches_info["助理教練"]
            trainer = coaches_info["訓練師"]
            # 將球隊的教練信息轉換成文字格式
            coach_text = f"總教練: {team_name}隊 {head_coach}\n"
            coach_text += f'助理教練: {", ".join(assistant_coach)}\n'
            coach_text += f"訓練師: {', '.join(trainer)}\n"
            content_arr = [TextSendMessage(f"以下是{team_name}隊的教練團\n{coach_text}")]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "公鹿教練":
        content_arr = []
        team_name = "公鹿"
        coaches_info = BucksCoach(html_bucks, team_name)
        if coaches_info:
            # 教練信息包括總教練、副教練、助理教練和訓練師
            head_coach = coaches_info["總教練"]
            assistant_coach = coaches_info["助理教練"]
            trainer = coaches_info["訓練師"]
            # 將球隊的教練信息轉換成文字格式
            coach_text = f"總教練: {team_name}隊 {head_coach}\n"
            coach_text += f'助理教練: {", ".join(assistant_coach)}\n'
            coach_text += f"訓練師: {', '.join(trainer)}\n"
            content_arr = [TextSendMessage(f"以下是{team_name}隊的教練團\n{coach_text}")]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "灰狼教練":
        content_arr = []
        team_name = "灰狼"
        coaches_info = TimberwolvesCoach(html_timberwolves, team_name)
        if coaches_info:
            # 教練信息包括總教練、副教練、助理教練和訓練師
            head_coach = coaches_info["總教練"]
            assistant_coach = coaches_info["助理教練"]
            trainer = coaches_info["訓練師"]
            # 將球隊的教練信息轉換成文字格式
            coach_text = f"總教練: {team_name}隊 {head_coach}\n"
            coach_text += f'助理教練: {", ".join(assistant_coach)}\n'
            coach_text += f"訓練師: {', '.join(trainer)}\n"
            content_arr = [TextSendMessage(f"以下是{team_name}隊的教練團\n{coach_text}")]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "爵士教練":
        content_arr = []
        team_name = "爵士"
        coaches_info = JazzCoach(html_jazz, team_name)
        if coaches_info:
            # 教練信息包括總教練、副教練、助理教練和訓練師
            head_coach = coaches_info["總教練"]
            assistant_coach = coaches_info["助理教練"]
            trainer = coaches_info["訓練師"]
            # 將球隊的教練信息轉換成文字格式
            coach_text = f"總教練: {team_name}隊 {head_coach}\n"
            coach_text += f'助理教練: {", ".join(assistant_coach)}\n'
            coach_text += f"訓練師: {', '.join(trainer)}\n"
            content_arr = [TextSendMessage(f"以下是{team_name}隊的教練團\n{coach_text}")]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "雷霆教練":
        content_arr = []
        team_name = "雷霆"
        coaches_info = ThunderCoach(html_thunder, team_name)
        if coaches_info:
            # 教練信息包括總教練、副教練、助理教練和訓練師
            head_coach = coaches_info["總教練"]
            assistant_coach = coaches_info["助理教練"]
            trainer = coaches_info["訓練師"]
            # 將球隊的教練信息轉換成文字格式
            coach_text = f"總教練: {team_name}隊 {head_coach}\n"
            coach_text += f'助理教練: {", ".join(assistant_coach)}\n'
            coach_text += f"訓練師: {', '.join(trainer)}\n"
            content_arr = [TextSendMessage(f"以下是{team_name}隊的教練團\n{coach_text}")]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "拓荒者教練":
        content_arr = []
        team_name = "拓荒者"
        coaches_info = BlazersCoach(html_blazers, team_name)
        if coaches_info:
            # 教練信息包括總教練、副教練、助理教練和訓練師
            head_coach = coaches_info["總教練"]
            assistant_coach = coaches_info["助理教練"]
            trainer = coaches_info["訓練師"]
            # 將球隊的教練信息轉換成文字格式
            coach_text = f"總教練: {team_name}隊 {head_coach}\n"
            coach_text += f'助理教練: {", ".join(assistant_coach)}\n'
            coach_text += f"訓練師: {', '.join(trainer)}\n"
            content_arr = [TextSendMessage(f"以下是{team_name}隊的教練團\n{coach_text}")]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "金塊教練":
        content_arr = []
        team_name = "金塊"
        coaches_info = NuggetsCoach(html_nuggets, team_name)
        if coaches_info:
            # 教練信息包括總教練、副教練、助理教練和訓練師
            head_coach = coaches_info["總教練"]
            assistant_coach = coaches_info["助理教練"]
            trainer = coaches_info["訓練師"]
            # 將球隊的教練信息轉換成文字格式
            coach_text = f"總教練: {team_name}隊 {head_coach}\n"
            coach_text += f'助理教練: {", ".join(assistant_coach)}\n'
            coach_text += f"訓練師: {', '.join(trainer)}\n"
            content_arr = [TextSendMessage(f"以下是{team_name}隊的教練團\n{coach_text}")]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "灰熊教練":
        content_arr = []
        team_name = "灰熊"
        coaches_info = GrizzliesCoach(html_grizzlies, team_name)
        if coaches_info:
            # 教練信息包括總教練、副教練、助理教練和訓練師
            head_coach = coaches_info["總教練"]
            assistant_coach = coaches_info["助理教練"]
            trainer = coaches_info["訓練師"]
            # 將球隊的教練信息轉換成文字格式
            coach_text = f"總教練: {team_name}隊 {head_coach}\n"
            coach_text += f'助理教練: {", ".join(assistant_coach)}\n'
            coach_text += f"訓練師: {', '.join(trainer)}\n"
            content_arr = [TextSendMessage(f"以下是{team_name}隊的教練團\n{coach_text}")]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "火箭教練":
        content_arr = []
        team_name = "火箭"
        coaches_info = RocketsCoach(html_rockets, team_name)
        if coaches_info:
            # 教練信息包括總教練、副教練、助理教練和訓練師
            head_coach = coaches_info["總教練"]
            assistant_coach = coaches_info["助理教練"]
            trainer = coaches_info["訓練師"]
            # 將球隊的教練信息轉換成文字格式
            coach_text = f"總教練: {team_name}隊 {head_coach}\n"
            coach_text += f'助理教練: {", ".join(assistant_coach)}\n'
            coach_text += f"訓練師: {', '.join(trainer)}\n"
            content_arr = [TextSendMessage(f"以下是{team_name}隊的教練團\n{coach_text}")]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "鵜鶘教練":
        content_arr = []
        team_name = "鵜鶘"
        coaches_info = PelicansCoach(html_pelicans, team_name)
        if coaches_info:
            # 教練信息包括總教練、副教練、助理教練和訓練師
            head_coach = coaches_info["總教練"]
            assistant_coach = coaches_info["助理教練"]
            trainer = coaches_info["訓練師"]
            # 將球隊的教練信息轉換成文字格式
            coach_text = f"總教練: {team_name}隊 {head_coach}\n"
            coach_text += f'助理教練: {", ".join(assistant_coach)}\n'
            coach_text += f"訓練師: {', '.join(trainer)}\n"
            content_arr = [TextSendMessage(f"以下是{team_name}隊的教練團\n{coach_text}")]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "馬刺教練":
        content_arr = []
        team_name = "馬刺"
        coaches_info = SpursCoach(html_spurs, team_name)
        if coaches_info:
            # 教練信息包括總教練、副教練、助理教練和訓練師
            head_coach = coaches_info["總教練"]
            assistant_coach = coaches_info["助理教練"]
            trainer = coaches_info["訓練師"]
            # 將球隊的教練信息轉換成文字格式
            coach_text = f"總教練: {team_name}隊 {head_coach}\n"
            coach_text += f'助理教練: {", ".join(assistant_coach)}\n'
            coach_text += f"訓練師: {', '.join(trainer)}\n"
            content_arr = [TextSendMessage(f"以下是{team_name}隊的教練團\n{coach_text}")]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "獨行俠教練":
        content_arr = []
        team_name = "獨行俠"
        coaches_info = MavericksCoach(html_mavericks, team_name)
        if coaches_info:
            # 教練信息包括總教練、副教練、助理教練和訓練師
            head_coach = coaches_info["總教練"]
            assistant_coach = coaches_info["助理教練"]
            trainer = coaches_info["訓練師"]
            # 將球隊的教練信息轉換成文字格式
            coach_text = f"總教練: {team_name}隊 {head_coach}\n"
            coach_text += f'助理教練: {", ".join(assistant_coach)}\n'
            coach_text += f"訓練師: {', '.join(trainer)}\n"
            content_arr = [TextSendMessage(f"以下是{team_name}隊的教練團\n{coach_text}")]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "勇士教練":
        content_arr = []
        team_name = "勇士"
        coaches_info = WarriorsCoach(html_warriors, team_name)
        if coaches_info:
            # 教練信息包括總教練、副教練、助理教練和訓練師
            head_coach = coaches_info["總教練"]
            assistant_coach = coaches_info["助理教練"]
            trainer = coaches_info["訓練師"]
            # 將球隊的教練信息轉換成文字格式
            coach_text = f"總教練: {team_name}隊 {head_coach}\n"
            coach_text += f'助理教練: {", ".join(assistant_coach)}\n'
            coach_text += f"訓練師: {', '.join(trainer)}\n"
            content_arr = [TextSendMessage(f"以下是{team_name}隊的教練團\n{coach_text}")]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "湖人教練":
        content_arr = []
        team_name = "湖人"
        coaches_info = LakersCoach(html_lakers, team_name)
        if coaches_info:
            # 教練信息包括總教練、副教練、助理教練和訓練師
            head_coach = coaches_info["總教練"]
            assistant_coach = coaches_info["助理教練"]
            trainer = coaches_info["訓練師"]
            # 將球隊的教練信息轉換成文字格式
            coach_text = f"總教練: {team_name}隊 {head_coach}\n"
            coach_text += f'助理教練: {", ".join(assistant_coach)}\n'
            coach_text += f"訓練師: {', '.join(trainer)}\n"
            content_arr = [TextSendMessage(f"以下是{team_name}隊的教練團\n{coach_text}")]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "快艇教練":
        content_arr = []
        team_name = "快艇"
        coaches_info = ClippersCoach(html_clippers, team_name)
        if coaches_info:
            # 教練信息包括總教練、副教練、助理教練和訓練師
            head_coach = coaches_info["總教練"]
            assistant_coaches = coaches_info["副教練"]
            assistant_coach = coaches_info["助理教練"]
            trainer = coaches_info["訓練師"]
            # 將球隊的教練信息轉換成文字格式
            coach_text = f"總教練: {team_name}隊 {head_coach}\n"
            coach_text += f'副教練: {", ".join(assistant_coaches)}\n'
            coach_text += f'助理教練: {", ".join(assistant_coach)}\n'
            coach_text += f"訓練師: {', '.join(trainer)}\n"
            content_arr = [TextSendMessage(f"以下是{team_name}隊的教練團\n{coach_text}")]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "太陽教練":
        content_arr = []
        team_name = "太陽"
        coaches_info = SunsCoach(html_suns, team_name)
        if coaches_info:
            # 教練信息包括總教練、副教練、助理教練和訓練師
            head_coach = coaches_info["總教練"]
            assistant_coaches = coaches_info["副教練"]
            assistant_coach = coaches_info["助理教練"]
            trainer = coaches_info["訓練師"]
            # 將球隊的教練信息轉換成文字格式
            coach_text = f"總教練: {team_name}隊 {head_coach}\n"
            coach_text += f'副教練: {", ".join(assistant_coaches)}\n'
            coach_text += f'助理教練: {", ".join(assistant_coach)}\n'
            coach_text += f"訓練師: {', '.join(trainer)}\n"
            content_arr = [TextSendMessage(f"以下是{team_name}隊的教練團\n{coach_text}")]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "國王教練":
        content_arr = []
        team_name = "國王"
        coaches_info = KingsCoach(html_kings, team_name)
        if coaches_info:
            # 教練信息包括總教練、副教練、助理教練和訓練師
            head_coach = coaches_info["總教練"]
            assistant_coaches = coaches_info["副教練"]
            assistant_coach = coaches_info["助理教練"]
            # 將球隊的教練信息轉換成文字格式
            coach_text = f"總教練: {team_name}隊 {head_coach}\n"
            coach_text += f'副教練: {", ".join(assistant_coaches)}\n'
            coach_text += f'助理教練: {", ".join(assistant_coach)}\n'
            content_arr = [TextSendMessage(f"以下是{team_name}隊的教練團\n{coach_text}")]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "老鷹10月賽程":
        team_code = "hawks"  # 代碼
        month = 10
        hawks_schedule = GetAllTeamSchedules(team_code, month)  # 使用上一個回答中的函數

        if hawks_schedule:
            messages = hawks_schedule.get("老鷹")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"老鷹{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "老鷹11月賽程":
        team_code = "hawks"  # 代碼
        month = 11
        hawks_schedule = GetAllTeamSchedules(team_code, month)

        if hawks_schedule:
            messages = hawks_schedule.get("老鷹")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"老鷹{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "老鷹12月賽程":
        team_code = "hawks"  # 代碼
        month = 12
        hawks_schedule = GetAllTeamSchedules(team_code, month)

        if hawks_schedule:
            messages = hawks_schedule.get("老鷹")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"老鷹{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "老鷹1月賽程":
        team_code = "hawks"  # 代碼
        month = 1
        hawks_schedule = GetAllTeamSchedules(team_code, month)

        if hawks_schedule:
            messages = hawks_schedule.get("老鷹")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"老鷹{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "老鷹2月賽程":
        team_code = "hawks"  # 代碼
        month = 2
        hawks_schedule = GetAllTeamSchedules(team_code, month)

        if hawks_schedule:
            messages = hawks_schedule.get("老鷹")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"老鷹{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "老鷹3月賽程":
        team_code = "hawks"  # 代碼
        month = 3
        hawks_schedule = GetAllTeamSchedules(team_code, month)

        if hawks_schedule:
            messages = hawks_schedule.get("老鷹")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"老鷹{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "老鷹4月賽程":
        team_code = "hawks"  # 代碼
        month = 4
        hawks_schedule = GetAllTeamSchedules(team_code, month)

        if hawks_schedule:
            messages = hawks_schedule.get("老鷹")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"老鷹{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "塞爾提克10月賽程":
        team_code = "celtics"  # 代碼
        month = 10
        celtics_schedule = GetAllTeamSchedules(team_code, month)

        if celtics_schedule:
            messages = celtics_schedule.get("凱爾特人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"凱爾特人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "塞爾提克11月賽程":
        team_code = "celtics"  # 代碼
        month = 11
        celtics_schedule = GetAllTeamSchedules(team_code, month)
        if celtics_schedule:
            messages = celtics_schedule.get("凱爾特人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"凱爾特人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "塞爾提克12月賽程":
        team_code = "celtics"  # 代碼
        month = 12
        celtics_schedule = GetAllTeamSchedules(team_code, month)

        if celtics_schedule:
            messages = celtics_schedule.get("凱爾特人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"凱爾特人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "塞爾提克1月賽程":
        team_code = "celtics"  # 代碼
        month = 1
        celtics_schedule = GetAllTeamSchedules(team_code, month)

        if celtics_schedule:
            messages = celtics_schedule.get("凱爾特人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"凱爾特人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "塞爾提克2月賽程":
        team_code = "celtics"  # 代碼
        month = 2
        celtics_schedule = GetAllTeamSchedules(team_code, month)

        if celtics_schedule:
            messages = celtics_schedule.get("凱爾特人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"凱爾特人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "塞爾提克3月賽程":
        team_code = "celtics"  # 代碼
        month = 3
        celtics_schedule = GetAllTeamSchedules(team_code, month)

        if celtics_schedule:
            messages = celtics_schedule.get("凱爾特人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"凱爾特人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "塞爾提克4月賽程":
        team_code = "celtics"  # 代碼
        month = 4
        celtics_schedule = GetAllTeamSchedules(team_code, month)

        if celtics_schedule:
            messages = celtics_schedule.get("凱爾特人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"凱爾特人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "公牛10月賽程":
        team_code = "bulls"  # 代碼
        month = 10
        bulls_schedule = GetAllTeamSchedules(team_code, month)

        if bulls_schedule:
            messages = bulls_schedule.get("公牛")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"公牛{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "公牛11月賽程":
        team_code = "bulls"  # 代碼
        month = 11
        bulls_schedule = GetAllTeamSchedules(team_code, month)

        if bulls_schedule:
            messages = bulls_schedule.get("公牛")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"公牛{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "公牛12月賽程":
        team_code = "bulls"  # 代碼
        month = 12
        bulls_schedule = GetAllTeamSchedules(team_code, month)

        if bulls_schedule:
            messages = bulls_schedule.get("公牛")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"公牛{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "公牛1月賽程":
        team_code = "bulls"  # 代碼
        month = 1
        bulls_schedule = GetAllTeamSchedules(team_code, month)

        if bulls_schedule:
            messages = bulls_schedule.get("公牛")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"公牛{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "公牛2月賽程":
        team_code = "bulls"  # 代碼
        month = 2
        bulls_schedule = GetAllTeamSchedules(team_code, month)

        if bulls_schedule:
            messages = bulls_schedule.get("公牛")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"公牛{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "公牛3月賽程":
        team_code = "bulls"  # 代碼
        month = 3
        bulls_schedule = GetAllTeamSchedules(team_code, month)

        if bulls_schedule:
            messages = bulls_schedule.get("公牛")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"公牛{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "公牛4月賽程":
        team_code = "bulls"  # 代碼
        month = 4
        bulls_schedule = GetAllTeamSchedules(team_code, month)

        if bulls_schedule:
            messages = bulls_schedule.get("公牛")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"公牛{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "黃蜂10月賽程":
        team_code = "hornets"  # 代碼
        month = 10
        hornets_schedule = GetAllTeamSchedules(team_code, month)

        if hornets_schedule:
            messages = hornets_schedule.get("黃蜂")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"黃蜂{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "黃蜂11月賽程":
        team_code = "hornets"  # 代碼
        month = 11
        hornets_schedule = GetAllTeamSchedules(team_code, month)

        if hornets_schedule:
            messages = hornets_schedule.get("黃蜂")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"黃蜂{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "黃蜂12月賽程":
        team_code = "hornets"  # 代碼
        month = 12
        hornets_schedule = GetAllTeamSchedules(team_code, month)

        if hornets_schedule:
            messages = hornets_schedule.get("黃蜂")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"黃蜂{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "黃蜂1月賽程":
        team_code = "hornets"  # 代碼
        month = 1
        hornets_schedule = GetAllTeamSchedules(team_code, month)

        if hornets_schedule:
            messages = hornets_schedule.get("黃蜂")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"黃蜂{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "黃蜂2月賽程":
        team_code = "hornets"  # 代碼
        month = 2
        hornets_schedule = GetAllTeamSchedules(team_code, month)
        if hornets_schedule:
            messages = hornets_schedule.get("黃蜂")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"黃蜂{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "黃蜂3月賽程":
        team_code = "hornets"  # 代碼
        month = 3
        hornets_schedule = GetAllTeamSchedules(team_code, month)

        if hornets_schedule:
            messages = hornets_schedule.get("黃蜂")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"黃蜂{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "黃蜂4月賽程":
        team_code = "hornets"  # 代碼
        month = 4
        hornets_schedule = GetAllTeamSchedules(team_code, month)

        if hornets_schedule:
            messages = hornets_schedule.get("黃蜂")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"黃蜂{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "籃網10月賽程":
        team_code = "nets"  # 代碼
        month = 10
        nets_schedule = GetAllTeamSchedules(team_code, month)

        if nets_schedule:
            messages = nets_schedule.get("籃網")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"籃網{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "籃網11月賽程":
        team_code = "nets"  # 代碼
        month = 11
        nets_schedule = GetAllTeamSchedules(team_code, month)

        if nets_schedule:
            messages = nets_schedule.get("籃網")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"籃網{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "籃網12月賽程":
        team_code = "nets"  # 代碼
        month = 12
        nets_schedule = GetAllTeamSchedules(team_code, month)

        if nets_schedule:
            messages = nets_schedule.get("籃網")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"籃網{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "籃網1月賽程":
        team_code = "nets"  # 代碼
        month = 1
        nets_schedule = GetAllTeamSchedules(team_code, month)

        if nets_schedule:
            messages = nets_schedule.get("籃網")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"籃網{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "籃網2月賽程":
        team_code = "nets"  # 代碼
        month = 2
        nets_schedule = GetAllTeamSchedules(team_code, month)

        if nets_schedule:
            messages = nets_schedule.get("籃網")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"籃網{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "籃網3月賽程":
        team_code = "nets"  # 代碼
        month = 3
        nets_schedule = GetAllTeamSchedules(team_code, month)

        if nets_schedule:
            messages = nets_schedule.get("籃網")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"籃網{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "籃網4月賽程":
        team_code = "nets"  # 代碼
        month = 4
        nets_schedule = GetAllTeamSchedules(team_code, month)

        if nets_schedule:
            messages = nets_schedule.get("籃網")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"籃網{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "騎士10月賽程":
        team_code = "cavaliers"  # 代碼
        month = 10
        cavaliers_schedule = GetAllTeamSchedules(team_code, month)

        if cavaliers_schedule:
            messages = cavaliers_schedule.get("騎士")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"騎士{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "騎士11月賽程":
        team_code = "cavaliers"  # 代碼
        month = 11
        cavaliers_schedule = GetAllTeamSchedules(team_code, month)

        if cavaliers_schedule:
            messages = cavaliers_schedule.get("騎士")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"騎士{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "騎士12月賽程":
        team_code = "cavaliers"  # 代碼
        month = 12
        cavaliers_schedule = GetAllTeamSchedules(team_code, month)

        if cavaliers_schedule:
            messages = cavaliers_schedule.get("騎士")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"騎士{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "騎士1月賽程":
        team_code = "cavaliers"  # 代碼
        month = 1
        cavaliers_schedule = GetAllTeamSchedules(team_code, month)

        if cavaliers_schedule:
            messages = cavaliers_schedule.get("騎士")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"騎士{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "騎士2月賽程":
        team_code = "cavaliers"  # 代碼
        month = 2
        cavaliers_schedule = GetAllTeamSchedules(team_code, month)

        if cavaliers_schedule:
            messages = cavaliers_schedule.get("騎士")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"騎士{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "騎士3月賽程":
        team_code = "cavaliers"  # 代碼
        month = 3
        cavaliers_schedule = GetAllTeamSchedules(team_code, month)

        if cavaliers_schedule:
            messages = cavaliers_schedule.get("騎士")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"騎士{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "騎士4月賽程":
        team_code = "cavaliers"  # 代碼
        month = 4
        cavaliers_schedule = GetAllTeamSchedules(team_code, month)

        if cavaliers_schedule:
            messages = cavaliers_schedule.get("騎士")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"騎士{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "熱火10月賽程":
        team_code = "heat"  # 代碼
        month = 10
        heat_schedule = GetAllTeamSchedules(team_code, month)

        if heat_schedule:
            messages = heat_schedule.get("熱火")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"熱火{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "熱火11月賽程":
        team_code = "heat"  # 代碼
        month = 11
        heat_schedule = GetAllTeamSchedules(team_code, month)

        if heat_schedule:
            messages = heat_schedule.get("熱火")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"熱火{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "熱火12月賽程":
        team_code = "heat"  # 代碼
        month = 12
        heat_schedule = GetAllTeamSchedules(team_code, month)

        if heat_schedule:
            messages = heat_schedule.get("熱火")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"熱火{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "熱火1月賽程":
        team_code = "heat"  # 代碼
        month = 1
        heat_schedule = GetAllTeamSchedules(team_code, month)

        if heat_schedule:
            messages = heat_schedule.get("熱火")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"熱火{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "熱火2月賽程":
        team_code = "heat"  # 代碼
        month = 2
        heat_schedule = GetAllTeamSchedules(team_code, month)

        if heat_schedule:
            messages = heat_schedule.get("熱火")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"熱火{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "熱火3月賽程":
        team_code = "heat"  # 代碼
        month = 3
        heat_schedule = GetAllTeamSchedules(team_code, month)

        if heat_schedule:
            messages = heat_schedule.get("熱火")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"熱火{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "熱火4月賽程":
        team_code = "heat"  # 代碼
        month = 4
        heat_schedule = GetAllTeamSchedules(team_code, month)

        if heat_schedule:
            messages = heat_schedule.get("熱火")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"熱火{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "尼克10月賽程":
        team_code = "knicks"  # 代碼
        month = 10
        knicks_schedule = GetAllTeamSchedules(team_code, month)

        if knicks_schedule:
            messages = knicks_schedule.get("尼克斯")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"尼克斯{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "尼克11月賽程":
        team_code = "knicks"  # 代碼
        month = 11
        knicks_schedule = GetAllTeamSchedules(team_code, month)

        if knicks_schedule:
            messages = knicks_schedule.get("尼克斯")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"尼克斯{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "尼克12月賽程":
        team_code = "knicks"  # 代碼
        month = 12
        knicks_schedule = GetAllTeamSchedules(team_code, month)

        if knicks_schedule:
            messages = knicks_schedule.get("尼克斯")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"尼克斯{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "尼克1月賽程":
        team_code = "knicks"  # 代碼
        month = 1
        knicks_schedule = GetAllTeamSchedules(team_code, month)

        if knicks_schedule:
            messages = knicks_schedule.get("尼克斯")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"尼克斯{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "尼克2月賽程":
        team_code = "knicks"  # 代碼
        month = 2
        knicks_schedule = GetAllTeamSchedules(team_code, month)

        if knicks_schedule:
            messages = knicks_schedule.get("尼克斯")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"尼克斯{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "尼克3月賽程":
        team_code = "knicks"  # 代碼
        month = 3
        knicks_schedule = GetAllTeamSchedules(team_code, month)

        if knicks_schedule:
            messages = knicks_schedule.get("尼克斯")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"尼克斯{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "尼克4月賽程":
        team_code = "knicks"  # 代碼
        month = 4
        knicks_schedule = GetAllTeamSchedules(team_code, month)

        if knicks_schedule:
            messages = knicks_schedule.get("尼克斯")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"尼克斯{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "活塞10月賽程":
        team_code = "pistons"  # 代碼
        month = 10
        pistons_schedule = GetAllTeamSchedules(team_code, month)

        if pistons_schedule:
            messages = pistons_schedule.get("活塞")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"活塞{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "活塞11月賽程":
        team_code = "pistons"  # 代碼
        month = 11
        pistons_schedule = GetAllTeamSchedules(team_code, month)

        if pistons_schedule:
            messages = pistons_schedule.get("活塞")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"活塞{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "活塞12月賽程":
        team_code = "pistons"  # 代碼
        month = 12
        pistons_schedule = GetAllTeamSchedules(team_code, month)

        if pistons_schedule:
            messages = pistons_schedule.get("活塞")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"活塞{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "活塞1月賽程":
        team_code = "pistons"  # 代碼
        month = 1
        pistons_schedule = GetAllTeamSchedules(team_code, month)

        if pistons_schedule:
            messages = pistons_schedule.get("活塞")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"活塞{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "活塞2月賽程":
        team_code = "pistons"  # 代碼
        month = 2
        pistons_schedule = GetAllTeamSchedules(team_code, month)

        if pistons_schedule:
            messages = pistons_schedule.get("活塞")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"活塞{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "活塞3月賽程":
        team_code = "pistons"  # 代碼
        month = 3
        pistons_schedule = GetAllTeamSchedules(team_code, month)

        if pistons_schedule:
            messages = pistons_schedule.get("活塞")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"活塞{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "活塞4月賽程":
        team_code = "pistons"  # 代碼
        month = 4
        pistons_schedule = GetAllTeamSchedules(team_code, month)

        if pistons_schedule:
            messages = pistons_schedule.get("活塞")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"活塞{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "魔術10月賽程":
        team_code = "magic"  # 代碼
        month = 10
        magic_schedule = GetAllTeamSchedules(team_code, month)

        if magic_schedule:
            messages = magic_schedule.get("魔術")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"魔術{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "魔術11月賽程":
        team_code = "magic"  # 代碼
        month = 11
        magic_schedule = GetAllTeamSchedules(team_code, month)

        if magic_schedule:
            messages = magic_schedule.get("魔術")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"魔術{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "魔術12月賽程":
        team_code = "magic"  # 代碼
        month = 12
        magic_schedule = GetAllTeamSchedules(team_code, month)

        if magic_schedule:
            messages = magic_schedule.get("魔術")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"魔術{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "魔術1月賽程":
        team_code = "magic"  # 代碼
        month = 1
        magic_schedule = GetAllTeamSchedules(team_code, month)

        if magic_schedule:
            messages = magic_schedule.get("魔術")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"魔術{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "魔術2月賽程":
        team_code = "magic"  # 代碼
        month = 2
        magic_schedule = GetAllTeamSchedules(team_code, month)

        if magic_schedule:
            messages = magic_schedule.get("魔術")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"魔術{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "魔術3月賽程":
        team_code = "magic"  # 代碼
        month = 3
        magic_schedule = GetAllTeamSchedules(team_code, month)

        if magic_schedule:
            messages = magic_schedule.get("魔術")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"魔術{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "魔術4月賽程":
        team_code = "magic"  # 代碼
        month = 4
        magic_schedule = GetAllTeamSchedules(team_code, month)

        if magic_schedule:
            messages = magic_schedule.get("魔術")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"魔術{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "溜馬10月賽程":
        team_code = "pacers"  # 代碼
        month = 10
        pacers_schedule = GetAllTeamSchedules(team_code, month)

        if pacers_schedule:
            messages = pacers_schedule.get("步行者")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"步行者{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "溜馬11月賽程":
        team_code = "pacers"  # 代碼
        month = 11
        pacers_schedule = GetAllTeamSchedules(team_code, month)

        if pacers_schedule:
            messages = pacers_schedule.get("步行者")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"步行者{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "溜馬12月賽程":
        team_code = "pacers"  # 代碼
        month = 12
        pacers_schedule = GetAllTeamSchedules(team_code, month)

        if pacers_schedule:
            messages = pacers_schedule.get("步行者")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"步行者{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "溜馬1月賽程":
        team_code = "pacers"  # 代碼
        month = 1
        pacers_schedule = GetAllTeamSchedules(team_code, month)

        if pacers_schedule:
            messages = pacers_schedule.get("步行者")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"步行者{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "溜馬2月賽程":
        team_code = "pacers"  # 代碼
        month = 2
        pacers_schedule = GetAllTeamSchedules(team_code, month)

        if pacers_schedule:
            messages = pacers_schedule.get("步行者")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"步行者{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "溜馬3月賽程":
        team_code = "pacers"  # 代碼
        month = 3
        pacers_schedule = GetAllTeamSchedules(team_code, month)

        if pacers_schedule:
            messages = pacers_schedule.get("步行者")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"步行者{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "溜馬4月賽程":
        team_code = "pacers"  # 代碼
        month = 4
        pacers_schedule = GetAllTeamSchedules(team_code, month)

        if pacers_schedule:
            messages = pacers_schedule.get("步行者")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"步行者{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "巫師10月賽程":
        team_code = "wizards"  # 代碼
        month = 10
        wizards_schedule = GetAllTeamSchedules(team_code, month)

        if wizards_schedule:
            messages = wizards_schedule.get("奇才")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"奇才{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "巫師11月賽程":
        team_code = "wizards"  # 代碼
        month = 11
        wizards_schedule = GetAllTeamSchedules(team_code, month)

        if wizards_schedule:
            messages = wizards_schedule.get("奇才")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"奇才{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "巫師12月賽程":
        team_code = "wizards"  # 代碼
        month = 12
        wizards_schedule = GetAllTeamSchedules(team_code, month)

        if wizards_schedule:
            messages = wizards_schedule.get("奇才")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"奇才{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "巫師1月賽程":
        team_code = "wizards"  # 代碼
        month = 1
        wizards_schedule = GetAllTeamSchedules(team_code, month)

        if wizards_schedule:
            messages = wizards_schedule.get("奇才")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"奇才{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "巫師2月賽程":
        team_code = "wizards"  # 代碼
        month = 2
        wizards_schedule = GetAllTeamSchedules(team_code, month)

        if wizards_schedule:
            messages = wizards_schedule.get("奇才")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"奇才{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "巫師3月賽程":
        team_code = "wizards"  # 代碼
        month = 3
        wizards_schedule = GetAllTeamSchedules(team_code, month)

        if wizards_schedule:
            messages = wizards_schedule.get("奇才")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"奇才{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "巫師4月賽程":
        team_code = "wizards"  # 代碼
        month = 4
        wizards_schedule = GetAllTeamSchedules(team_code, month)

        if wizards_schedule:
            messages = wizards_schedule.get("奇才")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"奇才{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "暴龍10月賽程":
        team_code = "raptors"  # 代碼
        month = 10
        raptors_schedule = GetAllTeamSchedules(team_code, month)

        if raptors_schedule:
            messages = raptors_schedule.get("猛龍")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"猛龍{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "暴龍11月賽程":
        team_code = "raptors"  # 代碼
        month = 11
        raptors_schedule = GetAllTeamSchedules(team_code, month)

        if raptors_schedule:
            messages = raptors_schedule.get("猛龍")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"猛龍{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "暴龍12月賽程":
        team_code = "raptors"  # 代碼
        month = 12
        raptors_schedule = GetAllTeamSchedules(team_code, month)

        if raptors_schedule:
            messages = raptors_schedule.get("猛龍")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"猛龍{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "暴龍1月賽程":
        team_code = "raptors"  # 代碼
        month = 1
        raptors_schedule = GetAllTeamSchedules(team_code, month)

        if raptors_schedule:
            messages = raptors_schedule.get("猛龍")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"猛龍{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "暴龍2月賽程":
        team_code = "raptors"  # 代碼
        month = 2
        raptors_schedule = GetAllTeamSchedules(team_code, month)

        if raptors_schedule:
            messages = raptors_schedule.get("猛龍")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"猛龍{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "暴龍3月賽程":
        team_code = "raptors"  # 代碼
        month = 3
        raptors_schedule = GetAllTeamSchedules(team_code, month)

        if raptors_schedule:
            messages = raptors_schedule.get("猛龍")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"猛龍{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "暴龍4月賽程":
        team_code = "raptors"  # 代碼
        month = 4
        raptors_schedule = GetAllTeamSchedules(team_code, month)

        if raptors_schedule:
            messages = raptors_schedule.get("猛龍")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"猛龍{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "公鹿10月賽程":
        team_code = "bucks"  # 代碼
        month = 10
        bucks_schedule = GetAllTeamSchedules(team_code, month)

        if bucks_schedule:
            messages = bucks_schedule.get("雄鹿")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"雄鹿{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "公鹿11月賽程":
        team_code = "bucks"  # 代碼
        month = 11
        bucks_schedule = GetAllTeamSchedules(team_code, month)

        if bucks_schedule:
            messages = bucks_schedule.get("雄鹿")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"雄鹿{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "公鹿12月賽程":
        team_code = "bucks"  # 代碼
        month = 12
        bucks_schedule = GetAllTeamSchedules(team_code, month)

        if bucks_schedule:
            messages = bucks_schedule.get("雄鹿")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"雄鹿{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "公鹿1月賽程":
        team_code = "bucks"  # 代碼
        month = 1
        bucks_schedule = GetAllTeamSchedules(team_code, month)

        if bucks_schedule:
            messages = bucks_schedule.get("雄鹿")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"雄鹿{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "公鹿2月賽程":
        team_code = "bucks"  # 代碼
        month = 2
        bucks_schedule = GetAllTeamSchedules(team_code, month)

        if bucks_schedule:
            messages = bucks_schedule.get("雄鹿")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"雄鹿{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "公鹿3月賽程":
        team_code = "bucks"  # 代碼
        month = 3
        bucks_schedule = GetAllTeamSchedules(team_code, month)

        if bucks_schedule:
            messages = bucks_schedule.get("雄鹿")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"雄鹿{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "公鹿4月賽程":
        team_code = "bucks"  # 代碼
        month = 4
        bucks_schedule = GetAllTeamSchedules(team_code, month)

        if bucks_schedule:
            messages = bucks_schedule.get("雄鹿")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"雄鹿{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "獨行俠10月賽程":
        team_code = "mavericks"  # 代碼
        month = 10
        mavericks_schedule = GetAllTeamSchedules(team_code, month)

        if mavericks_schedule:
            messages = mavericks_schedule.get("獨行俠")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"獨行俠{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "獨行俠11月賽程":
        team_code = "mavericks"  # 代碼
        month = 11
        mavericks_schedule = GetAllTeamSchedules(team_code, month)

        if mavericks_schedule:
            messages = mavericks_schedule.get("獨行俠")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"獨行俠{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "獨行俠12月賽程":
        team_code = "mavericks"  # 代碼
        month = 12
        mavericks_schedule = GetAllTeamSchedules(team_code, month)

        if mavericks_schedule:
            messages = mavericks_schedule.get("獨行俠")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"獨行俠{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "獨行俠1月賽程":
        team_code = "mavericks"  # 代碼
        month = 1
        mavericks_schedule = GetAllTeamSchedules(team_code, month)

        if mavericks_schedule:
            messages = mavericks_schedule.get("獨行俠")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"獨行俠{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "獨行俠2月賽程":
        team_code = "mavericks"  # 代碼
        month = 2
        mavericks_schedule = GetAllTeamSchedules(team_code, month)

        if mavericks_schedule:
            messages = mavericks_schedule.get("獨行俠")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"獨行俠{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "獨行俠3月賽程":
        team_code = "mavericks"  # 代碼
        month = 3
        mavericks_schedule = GetAllTeamSchedules(team_code, month)

        if mavericks_schedule:
            messages = mavericks_schedule.get("獨行俠")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"獨行俠{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "獨行俠4月賽程":
        team_code = "mavericks"  # 代碼
        month = 4
        mavericks_schedule = GetAllTeamSchedules(team_code, month)

        if mavericks_schedule:
            messages = mavericks_schedule.get("獨行俠")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"獨行俠{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "金塊10月賽程":
        team_code = "nuggets"  # 代碼
        month = 10
        nuggets_schedule = GetAllTeamSchedules(team_code, month)

        if nuggets_schedule:
            messages = nuggets_schedule.get("掘金")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"掘金{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "金塊11月賽程":
        team_code = "nuggets"  # 代碼
        month = 11
        nuggets_schedule = GetAllTeamSchedules(team_code, month)

        if nuggets_schedule:
            messages = nuggets_schedule.get("掘金")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"掘金{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "金塊12月賽程":
        team_code = "nuggets"  # 代碼
        month = 12
        nuggets_schedule = GetAllTeamSchedules(team_code, month)

        if nuggets_schedule:
            messages = nuggets_schedule.get("掘金")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"掘金{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "金塊1月賽程":
        team_code = "nuggets"  # 代碼
        month = 1
        nuggets_schedule = GetAllTeamSchedules(team_code, month)

        if nuggets_schedule:
            messages = nuggets_schedule.get("掘金")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"掘金{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "金塊2月賽程":
        team_code = "nuggets"  # 代碼
        month = 2
        nuggets_schedule = GetAllTeamSchedules(team_code, month)

        if nuggets_schedule:
            messages = nuggets_schedule.get("掘金")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"掘金{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "金塊3月賽程":
        team_code = "nuggets"  # 代碼
        month = 3
        nuggets_schedule = GetAllTeamSchedules(team_code, month)

        if nuggets_schedule:
            messages = nuggets_schedule.get("掘金")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"掘金{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "金塊4月賽程":
        team_code = "nuggets"  # 代碼
        month = 4
        nuggets_schedule = GetAllTeamSchedules(team_code, month)

        if nuggets_schedule:
            messages = nuggets_schedule.get("掘金")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"掘金{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "勇士10月賽程":
        team_code = "warriors"  # 代碼
        month = 10
        warriors_schedule = GetAllTeamSchedules(team_code, month)

        if warriors_schedule:
            messages = warriors_schedule.get("勇士")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"勇士{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "勇士11月賽程":
        team_code = "warriors"  # 代碼
        month = 11
        warriors_schedule = GetAllTeamSchedules(team_code, month)

        if warriors_schedule:
            messages = warriors_schedule.get("勇士")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"勇士{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "勇士12月賽程":
        team_code = "warriors"  # 代碼
        month = 12
        warriors_schedule = GetAllTeamSchedules(team_code, month)

        if warriors_schedule:
            messages = warriors_schedule.get("勇士")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"勇士{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "勇士1月賽程":
        team_code = "warriors"  # 代碼
        month = 1
        warriors_schedule = GetAllTeamSchedules(team_code, month)

        if warriors_schedule:
            messages = warriors_schedule.get("勇士")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"勇士{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "勇士2月賽程":
        team_code = "warriors"  # 代碼
        month = 2
        warriors_schedule = GetAllTeamSchedules(team_code, month)

        if warriors_schedule:
            messages = warriors_schedule.get("勇士")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"勇士{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "勇士3月賽程":
        team_code = "warriors"  # 代碼
        month = 3
        warriors_schedule = GetAllTeamSchedules(team_code, month)

        if warriors_schedule:
            messages = warriors_schedule.get("勇士")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"勇士{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "勇士4月賽程":
        team_code = "warriors"  # 代碼
        month = 4
        warriors_schedule = GetAllTeamSchedules(team_code, month)

        if warriors_schedule:
            messages = warriors_schedule.get("勇士")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"勇士{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "火箭10月賽程":
        team_code = "rockets"  # 代碼
        month = 10
        rockets_schedule = GetAllTeamSchedules(team_code, month)

        if rockets_schedule:
            messages = rockets_schedule.get("火箭")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"火箭{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "火箭11月賽程":
        team_code = "rockets"  # 代碼
        month = 11
        rockets_schedule = GetAllTeamSchedules(team_code, month)

        if rockets_schedule:
            messages = rockets_schedule.get("火箭")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"火箭{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "火箭12月賽程":
        team_code = "rockets"  # 代碼
        month = 12
        rockets_schedule = GetAllTeamSchedules(team_code, month)

        if rockets_schedule:
            messages = rockets_schedule.get("火箭")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"火箭{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "火箭1月賽程":
        team_code = "rockets"  # 代碼
        month = 1
        rockets_schedule = GetAllTeamSchedules(team_code, month)

        if rockets_schedule:
            messages = rockets_schedule.get("火箭")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"火箭{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "火箭2月賽程":
        team_code = "rockets"  # 代碼
        month = 2
        rockets_schedule = GetAllTeamSchedules(team_code, month)

        if rockets_schedule:
            messages = rockets_schedule.get("火箭")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"火箭{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "火箭3月賽程":
        team_code = "rockets"  # 代碼
        month = 3
        rockets_schedule = GetAllTeamSchedules(team_code, month)

        if rockets_schedule:
            messages = rockets_schedule.get("火箭")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"火箭{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "火箭4月賽程":
        team_code = "rockets"  # 代碼
        month = 4
        rockets_schedule = GetAllTeamSchedules(team_code, month)

        if rockets_schedule:
            messages = rockets_schedule.get("火箭")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"火箭{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "灰狼10月賽程":
        team_code = "timberwolves"  # 代碼
        month = 10
        timberwolves_schedule = GetAllTeamSchedules(team_code, month)

        if timberwolves_schedule:
            messages = timberwolves_schedule.get("森林狼")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"森林狼{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "灰狼11月賽程":
        team_code = "timberwolves"  # 代碼
        month = 11
        timberwolves_schedule = GetAllTeamSchedules(team_code, month)

        if timberwolves_schedule:
            messages = timberwolves_schedule.get("森林狼")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"森林狼{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "灰狼12月賽程":
        team_code = "timberwolves"  # 代碼
        month = 12
        timberwolves_schedule = GetAllTeamSchedules(team_code, month)

        if timberwolves_schedule:
            messages = timberwolves_schedule.get("森林狼")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"森林狼{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "灰狼1月賽程":
        team_code = "timberwolves"  # 代碼
        month = 1
        timberwolves_schedule = GetAllTeamSchedules(team_code, month)

        if timberwolves_schedule:
            messages = timberwolves_schedule.get("森林狼")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"森林狼{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "灰狼2月賽程":
        team_code = "timberwolves"  # 代碼
        month = 2
        timberwolves_schedule = GetAllTeamSchedules(team_code, month)

        if timberwolves_schedule:
            messages = timberwolves_schedule.get("森林狼")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"森林狼{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "灰狼3月賽程":
        team_code = "timberwolves"  # 代碼
        month = 3
        timberwolves_schedule = GetAllTeamSchedules(team_code, month)

        if timberwolves_schedule:
            messages = timberwolves_schedule.get("森林狼")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"森林狼{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "灰狼4月賽程":
        team_code = "timberwolves"  # 代碼
        month = 4
        timberwolves_schedule = GetAllTeamSchedules(team_code, month)

        if timberwolves_schedule:
            messages = timberwolves_schedule.get("森林狼")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"森林狼{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "快艇10月賽程":
        team_code = "clippers"  # 代碼
        month = 10
        clippers_schedule = GetAllTeamSchedules(team_code, month)

        if clippers_schedule:
            messages = clippers_schedule.get("快船")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"快船{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "快艇11月賽程":
        team_code = "clippers"  # 代碼
        month = 11
        clippers_schedule = GetAllTeamSchedules(team_code, month)

        if clippers_schedule:
            messages = clippers_schedule.get("快船")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"快船{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "快艇12月賽程":
        team_code = "clippers"  # 代碼
        month = 12
        clippers_schedule = GetAllTeamSchedules(team_code, month)

        if clippers_schedule:
            messages = clippers_schedule.get("快船")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"快船{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "快艇1月賽程":
        team_code = "clippers"  # 代碼
        month = 1
        clippers_schedule = GetAllTeamSchedules(team_code, month)

        if clippers_schedule:
            messages = clippers_schedule.get("快船")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"快船{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "快艇2月賽程":
        team_code = "clippers"  # 代碼
        month = 2
        clippers_schedule = GetAllTeamSchedules(team_code, month)

        if clippers_schedule:
            messages = clippers_schedule.get("快船")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"快船{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "快艇3月賽程":
        team_code = "clippers"  # 代碼
        month = 3
        clippers_schedule = GetAllTeamSchedules(team_code, month)

        if clippers_schedule:
            messages = clippers_schedule.get("快船")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"快船{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "快艇4月賽程":
        team_code = "clippers"  # 代碼
        month = 4
        clippers_schedule = GetAllTeamSchedules(team_code, month)

        if clippers_schedule:
            messages = clippers_schedule.get("快船")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"快船{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "灰熊10月賽程":
        team_code = "grizzlies"  # 代碼
        month = 10
        grizzlies_schedule = GetAllTeamSchedules(team_code, month)

        if grizzlies_schedule:
            messages = grizzlies_schedule.get("灰熊")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"灰熊{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "灰熊11月賽程":
        team_code = "grizzlies"  # 代碼
        month = 11
        grizzlies_schedule = GetAllTeamSchedules(team_code, month)

        if grizzlies_schedule:
            messages = grizzlies_schedule.get("灰熊")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"灰熊{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "灰熊12月賽程":
        team_code = "grizzlies"  # 代碼
        month = 12
        grizzlies_schedule = GetAllTeamSchedules(team_code, month)

        if grizzlies_schedule:
            messages = grizzlies_schedule.get("灰熊")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"灰熊{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "灰熊1月賽程":
        team_code = "grizzlies"  # 代碼
        month = 1
        grizzlies_schedule = GetAllTeamSchedules(team_code, month)

        if grizzlies_schedule:
            messages = grizzlies_schedule.get("灰熊")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"灰熊{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "灰熊2月賽程":
        team_code = "grizzlies"  # 代碼
        month = 2
        grizzlies_schedule = GetAllTeamSchedules(team_code, month)

        if grizzlies_schedule:
            messages = grizzlies_schedule.get("灰熊")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"灰熊{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "灰熊3月賽程":
        team_code = "grizzlies"  # 代碼
        month = 3
        grizzlies_schedule = GetAllTeamSchedules(team_code, month)

        if grizzlies_schedule:
            messages = grizzlies_schedule.get("灰熊")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"灰熊{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "灰熊4月賽程":
        team_code = "grizzlies"  # 代碼
        month = 4
        grizzlies_schedule = GetAllTeamSchedules(team_code, month)

        if grizzlies_schedule:
            messages = grizzlies_schedule.get("灰熊")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"灰熊{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "雷霆10月賽程":
        team_code = "thunder"  # 代碼
        month = 10
        thunder_schedule = GetAllTeamSchedules(team_code, month)

        if thunder_schedule:
            messages = thunder_schedule.get("雷霆")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"雷霆{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "雷霆11月賽程":
        team_code = "thunder"  # 代碼
        month = 11
        thunder_schedule = GetAllTeamSchedules(team_code, month)

        if thunder_schedule:
            messages = thunder_schedule.get("雷霆")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"雷霆{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "雷霆12月賽程":
        team_code = "thunder"  # 代碼
        month = 12
        thunder_schedule = GetAllTeamSchedules(team_code, month)

        if thunder_schedule:
            messages = thunder_schedule.get("雷霆")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"雷霆{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "雷霆1月賽程":
        team_code = "thunder"  # 代碼
        month = 1
        thunder_schedule = GetAllTeamSchedules(team_code, month)

        if thunder_schedule:
            messages = thunder_schedule.get("雷霆")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"雷霆{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "雷霆2月賽程":
        team_code = "thunder"  # 代碼
        month = 2
        thunder_schedule = GetAllTeamSchedules(team_code, month)

        if thunder_schedule:
            messages = thunder_schedule.get("雷霆")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"雷霆{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "雷霆3月賽程":
        team_code = "thunder"  # 代碼
        month = 3
        thunder_schedule = GetAllTeamSchedules(team_code, month)

        if thunder_schedule:
            messages = thunder_schedule.get("雷霆")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"雷霆{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "雷霆4月賽程":
        team_code = "thunder"  # 代碼
        month = 4
        thunder_schedule = GetAllTeamSchedules(team_code, month)

        if thunder_schedule:
            messages = thunder_schedule.get("雷霆")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"雷霆{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "湖人10月賽程":
        team_code = "lakers"  # 代碼
        month = 10
        lakers_schedule = GetAllTeamSchedules(team_code, month)

        if lakers_schedule:
            messages = lakers_schedule.get("湖人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"湖人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "湖人11月賽程":
        team_code = "lakers"  # 代碼
        month = 11
        lakers_schedule = GetAllTeamSchedules(team_code, month)

        if lakers_schedule:
            messages = lakers_schedule.get("湖人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"湖人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "湖人12月賽程":
        team_code = "lakers"  # 代碼
        month = 12
        lakers_schedule = GetAllTeamSchedules(team_code, month)

        if lakers_schedule:
            messages = lakers_schedule.get("湖人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"湖人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "湖人1月賽程":
        team_code = "lakers"  # 代碼
        month = 1
        lakers_schedule = GetAllTeamSchedules(team_code, month)

        if lakers_schedule:
            messages = lakers_schedule.get("湖人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"湖人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "湖人2月賽程":
        team_code = "lakers"  # 代碼
        month = 2
        lakers_schedule = GetAllTeamSchedules(team_code, month)

        if lakers_schedule:
            messages = lakers_schedule.get("湖人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"湖人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "湖人3月賽程":
        team_code = "lakers"  # 代碼
        month = 3
        lakers_schedule = GetAllTeamSchedules(team_code, month)

        if lakers_schedule:
            messages = lakers_schedule.get("湖人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"湖人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "湖人4月賽程":
        team_code = "lakers"  # 代碼
        month = 4
        lakers_schedule = GetAllTeamSchedules(team_code, month)

        if lakers_schedule:
            messages = lakers_schedule.get("湖人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"湖人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "鵜鶘10月賽程":
        team_code = "pelicans"  # 代碼
        month = 10
        pelicans_schedule = GetAllTeamSchedules(team_code, month)

        if pelicans_schedule:
            messages = pelicans_schedule.get("鵜鶘")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"鵜鶘{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "鵜鶘11月賽程":
        team_code = "pelicans"  # 代碼
        month = 11
        pelicans_schedule = GetAllTeamSchedules(team_code, month)

        if pelicans_schedule:
            messages = pelicans_schedule.get("鵜鶘")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"鵜鶘{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "鵜鶘12月賽程":
        team_code = "pelicans"  # 代碼
        month = 12
        pelicans_schedule = GetAllTeamSchedules(team_code, month)

        if pelicans_schedule:
            messages = pelicans_schedule.get("鵜鶘")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"鵜鶘{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "鵜鶘1月賽程":
        team_code = "pelicans"  # 代碼
        month = 1
        pelicans_schedule = GetAllTeamSchedules(team_code, month)

        if pelicans_schedule:
            messages = pelicans_schedule.get("鵜鶘")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"鵜鶘{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "鵜鶘2月賽程":
        team_code = "pelicans"  # 代碼
        month = 2
        pelicans_schedule = GetAllTeamSchedules(team_code, month)

        if pelicans_schedule:
            messages = pelicans_schedule.get("鵜鶘")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"鵜鶘{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "鵜鶘3月賽程":
        team_code = "pelicans"  # 代碼
        month = 3
        pelicans_schedule = GetAllTeamSchedules(team_code, month)

        if pelicans_schedule:
            messages = pelicans_schedule.get("鵜鶘")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"鵜鶘{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "鵜鶘4月賽程":
        team_code = "pelicans"  # 代碼
        month = 4
        pelicans_schedule = GetAllTeamSchedules(team_code, month)

        if pelicans_schedule:
            messages = pelicans_schedule.get("鵜鶘")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"鵜鶘{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "拓荒者10月賽程":
        team_code = "blazers"  # 代碼
        month = 10
        blazers_schedule = GetAllTeamSchedules(team_code, month)

        if blazers_schedule:
            messages = blazers_schedule.get("開拓者")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"開拓者{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "拓荒者11月賽程":
        team_code = "blazers"  # 代碼
        month = 11
        blazers_schedule = GetAllTeamSchedules(team_code, month)

        if blazers_schedule:
            messages = blazers_schedule.get("開拓者")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"開拓者{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "拓荒者12月賽程":
        team_code = "blazers"  # 代碼
        month = 12
        blazers_schedule = GetAllTeamSchedules(team_code, month)

        if blazers_schedule:
            messages = blazers_schedule.get("開拓者")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"開拓者{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "拓荒者1月賽程":
        team_code = "blazers"  # 代碼
        month = 1
        blazers_schedule = GetAllTeamSchedules(team_code, month)

        if blazers_schedule:
            messages = blazers_schedule.get("開拓者")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"開拓者{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "拓荒者2月賽程":
        team_code = "blazers"  # 代碼
        month = 2
        blazers_schedule = GetAllTeamSchedules(team_code, month)

        if blazers_schedule:
            messages = blazers_schedule.get("開拓者")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"開拓者{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "拓荒者3月賽程":
        team_code = "blazers"  # 代碼
        month = 3
        blazers_schedule = GetAllTeamSchedules(team_code, month)

        if blazers_schedule:
            messages = blazers_schedule.get("開拓者")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"開拓者{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "拓荒者4月賽程":
        team_code = "blazers"  # 代碼
        month = 4
        blazers_schedule = GetAllTeamSchedules(team_code, month)

        if blazers_schedule:
            messages = blazers_schedule.get("開拓者")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"開拓者{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "太陽10月賽程":
        team_code = "suns"  # 代碼
        month = 10
        suns_schedule = GetAllTeamSchedules(team_code, month)

        if suns_schedule:
            messages = suns_schedule.get("太陽")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"太陽{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "太陽11月賽程":
        team_code = "suns"  # 代碼
        month = 11
        suns_schedule = GetAllTeamSchedules(team_code, month)

        if suns_schedule:
            messages = suns_schedule.get("太陽")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"太陽{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "太陽12月賽程":
        team_code = "suns"  # 代碼
        month = 12
        suns_schedule = GetAllTeamSchedules(team_code, month)

        if suns_schedule:
            messages = suns_schedule.get("太陽")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"太陽{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "太陽1月賽程":
        team_code = "suns"  # 代碼
        month = 1
        suns_schedule = GetAllTeamSchedules(team_code, month)

        if suns_schedule:
            messages = suns_schedule.get("太陽")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"太陽{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "太陽2月賽程":
        team_code = "suns"  # 代碼
        month = 2
        suns_schedule = GetAllTeamSchedules(team_code, month)

        if suns_schedule:
            messages = suns_schedule.get("太陽")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"太陽{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "太陽3月賽程":
        team_code = "suns"  # 代碼
        month = 3
        suns_schedule = GetAllTeamSchedules(team_code, month)

        if suns_schedule:
            messages = suns_schedule.get("太陽")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"太陽{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "太陽4月賽程":
        team_code = "suns"  # 代碼
        month = 4
        suns_schedule = GetAllTeamSchedules(team_code, month)

        if suns_schedule:
            messages = suns_schedule.get("太陽")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"太陽{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "馬刺10月賽程":
        team_code = "spurs"  # 代碼
        month = 10
        spurs_schedule = GetAllTeamSchedules(team_code, month)

        if spurs_schedule:
            messages = spurs_schedule.get("馬刺")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"馬刺{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "馬刺11月賽程":
        team_code = "spurs"  # 代碼
        month = 11
        spurs_schedule = GetAllTeamSchedules(team_code, month)

        if spurs_schedule:
            messages = spurs_schedule.get("馬刺")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"馬刺{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "馬刺12月賽程":
        team_code = "spurs"  # 代碼
        month = 12
        spurs_schedule = GetAllTeamSchedules(team_code, month)

        if spurs_schedule:
            messages = spurs_schedule.get("馬刺")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"馬刺{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "馬刺1月賽程":
        team_code = "spurs"  # 代碼
        month = 1
        spurs_schedule = GetAllTeamSchedules(team_code, month)

        if spurs_schedule:
            messages = spurs_schedule.get("馬刺")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"馬刺{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "馬刺2月賽程":
        team_code = "spurs"  # 代碼
        month = 2
        spurs_schedule = GetAllTeamSchedules(team_code, month)

        if spurs_schedule:
            messages = spurs_schedule.get("馬刺")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"馬刺{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "馬刺3月賽程":
        team_code = "spurs"  # 代碼
        month = 3
        spurs_schedule = GetAllTeamSchedules(team_code, month)

        if spurs_schedule:
            messages = spurs_schedule.get("馬刺")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"馬刺{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "馬刺4月賽程":
        team_code = "spurs"  # 代碼
        month = 4
        spurs_schedule = GetAllTeamSchedules(team_code, month)

        if spurs_schedule:
            messages = spurs_schedule.get("馬刺")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"馬刺{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "爵士10月賽程":
        team_code = "jazz"  # 代碼
        month = 10
        jazz_schedule = GetAllTeamSchedules(team_code, month)

        if jazz_schedule:
            messages = jazz_schedule.get("爵士")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"爵士{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "爵士11月賽程":
        team_code = "jazz"  # 代碼
        month = 11
        jazz_schedule = GetAllTeamSchedules(team_code, month)

        if jazz_schedule:
            messages = jazz_schedule.get("爵士")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"爵士{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "爵士12月賽程":
        team_code = "jazz"  # 代碼
        month = 12
        jazz_schedule = GetAllTeamSchedules(team_code, month)

        if jazz_schedule:
            messages = jazz_schedule.get("爵士")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"爵士{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "爵士1月賽程":
        team_code = "jazz"  # 代碼
        month = 1
        jazz_schedule = GetAllTeamSchedules(team_code, month)

        if jazz_schedule:
            messages = jazz_schedule.get("爵士")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"爵士{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "爵士2月賽程":
        team_code = "jazz"  # 代碼
        month = 2
        jazz_schedule = GetAllTeamSchedules(team_code, month)

        if jazz_schedule:
            messages = jazz_schedule.get("爵士")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"爵士{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "爵士3月賽程":
        team_code = "jazz"  # 代碼
        month = 3
        jazz_schedule = GetAllTeamSchedules(team_code, month)

        if jazz_schedule:
            messages = jazz_schedule.get("爵士")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"爵士{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "爵士4月賽程":
        team_code = "jazz"  # 代碼
        month = 4
        jazz_schedule = GetAllTeamSchedules(team_code, month)

        if jazz_schedule:
            messages = jazz_schedule.get("爵士")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"爵士{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "國王10月賽程":
        team_code = "kings"  # 代碼
        month = 10
        kings_schedule = GetAllTeamSchedules(team_code, month)

        if kings_schedule:
            messages = kings_schedule.get("國王")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"國王{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "國王11月賽程":
        team_code = "kings"  # 代碼
        month = 11
        kings_schedule = GetAllTeamSchedules(team_code, month)

        if kings_schedule:
            messages = kings_schedule.get("國王")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"國王{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "國王12月賽程":
        team_code = "kings"  # 代碼
        month = 12
        kings_schedule = GetAllTeamSchedules(team_code, month)

        if kings_schedule:
            messages = kings_schedule.get("國王")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"國王{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "國王1月賽程":
        team_code = "kings"  # 代碼
        month = 1
        kings_schedule = GetAllTeamSchedules(team_code, month)

        if kings_schedule:
            messages = kings_schedule.get("國王")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"國王{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "國王2月賽程":
        team_code = "kings"  # 代碼
        month = 2
        kings_schedule = GetAllTeamSchedules(team_code, month)

        if kings_schedule:
            messages = kings_schedule.get("國王")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"國王{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "國王3月賽程":
        team_code = "kings"  # 代碼
        month = 3
        kings_schedule = GetAllTeamSchedules(team_code, month)

        if kings_schedule:
            messages = kings_schedule.get("國王")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"國王{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "國王4月賽程":
        team_code = "kings"  # 代碼
        month = 4
        kings_schedule = GetAllTeamSchedules(team_code, month)

        if kings_schedule:
            messages = kings_schedule.get("國王")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"國王{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "76人10月賽程":
        team_code = "76ers"  # 代碼
        month = 10
        phi_schedule = GetAllTeamSchedules(team_code, month)

        if phi_schedule:
            messages = phi_schedule.get("76人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"76人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "76人11月賽程":
        team_code = "76ers"  # 代碼
        month = 11
        phi_schedule = GetAllTeamSchedules(team_code, month)

        if phi_schedule:
            messages = phi_schedule.get("76人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"76人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "76人12月賽程":
        team_code = "76ers"  # 代碼
        month = 12
        phi_schedule = GetAllTeamSchedules(team_code, month)

        if phi_schedule:
            messages = phi_schedule.get("76人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"76人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "76人1月賽程":
        team_code = "76ers"  # 代碼
        month = 1
        phi_schedule = GetAllTeamSchedules(team_code, month)

        if phi_schedule:
            messages = phi_schedule.get("76人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"76人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "76人2月賽程":
        team_code = "76ers"  # 代碼
        month = 2
        phi_schedule = GetAllTeamSchedules(team_code, month)

        if phi_schedule:
            messages = phi_schedule.get("76人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"76人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "76人3月賽程":
        team_code = "76ers"  # 代碼
        month = 3
        phi_schedule = GetAllTeamSchedules(team_code, month)

        if phi_schedule:
            messages = phi_schedule.get("76人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"76人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "76人4月賽程":
        team_code = "76ers"  # 代碼
        month = 4
        phi_schedule = GetAllTeamSchedules(team_code, month)

        if phi_schedule:
            messages = phi_schedule.get("76人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"76人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "七六人10月賽程":
        team_code = "76ers"  # 代碼
        month = 10
        phi_schedule = GetAllTeamSchedules(team_code, month)

        if phi_schedule:
            messages = phi_schedule.get("76人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"76人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "七六人11月賽程":
        team_code = "76ers"  # 代碼
        month = 11
        phi_schedule = GetAllTeamSchedules(team_code, month)

        if phi_schedule:
            messages = phi_schedule.get("76人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"76人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "七六人12月賽程":
        team_code = "76ers"  # 代碼
        month = 12
        phi_schedule = GetAllTeamSchedules(team_code, month)

        if phi_schedule:
            messages = phi_schedule.get("76人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"76人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "七六人1月賽程":
        team_code = "76ers"  # 代碼
        month = 1
        phi_schedule = GetAllTeamSchedules(team_code, month)

        if phi_schedule:
            messages = phi_schedule.get("76人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"76人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "七六人2月賽程":
        team_code = "76ers"  # 代碼
        month = 2
        phi_schedule = GetAllTeamSchedules(team_code, month)

        if phi_schedule:
            messages = phi_schedule.get("76人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"76人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "七六人3月賽程":
        team_code = "76ers"  # 代碼
        month = 3
        phi_schedule = GetAllTeamSchedules(team_code, month)

        if phi_schedule:
            messages = phi_schedule.get("76人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"76人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "七六人4月賽程":
        team_code = "76ers"  # 代碼
        month = 4
        phi_schedule = GetAllTeamSchedules(team_code, month)

        if phi_schedule:
            messages = phi_schedule.get("76人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"76人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    

    if text == "賽程":
        content_arr = []
        content_arr.append(TextSendMessage("請輸入想要搜尋的隊伍\n加上月份賽程"))
        content_arr.append(TextSendMessage("例如:公鹿十月賽程"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "各球隊新聞":
        content_arr = []
        content_arr.append(TextSendMessage("請輸入想要搜尋的球隊加上新聞"))
        content_arr.append(TextSendMessage("例如:公鹿新聞"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "陣容":
        content_arr = []
        content_arr.append(TextSendMessage("請輸入想要搜尋的球隊加上陣容"))
        content_arr.append(TextSendMessage("例如:公鹿陣容"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0


    if text == "歷年數據":
        content_arr = []
        content_arr.append(TextSendMessage("請輸入月份加上球員數據"))
        content_arr.append(TextSendMessage("例如:202223LBJ數據"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "去年排名":
        content_arr = []
        content_arr.append(TextSendMessage("以下是2022-23賽季排名資訊"))
        content_arr.append(TextSendMessage("需要各別搜尋請先輸入去年在輸入球隊名稱加上排名"))
        content_arr.append(TextSendMessage("例如-去年勇士排名-"))
        content_arr.append(TextSendMessage(random_statement(去年賽季戰績)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "去年戰績":
        content_arr = []
        content_arr.append(TextSendMessage("以下是2022-23賽季戰績資訊"))
        content_arr.append(TextSendMessage("需要各別搜尋請先輸入去年在輸入球隊名稱加上戰績"))
        content_arr.append(TextSendMessage("例如-去年勇士戰績-"))
        content_arr.append(TextSendMessage(random_statement(去年賽季戰績)))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "今年排名":
        content_arr = []
        content_arr.append(TextSendMessage("以下提供給你所有球隊排名"))
        content_arr.append(TextSendMessage("需要各別搜尋請輸入\n球隊名稱加上排名"))
        content_arr.append(TextSendMessage("例如-勇士今年排名-"))
        content_arr.append(TextSendMessage(GetAllTeamStandings()))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "今年戰績":
        content_arr = []
        content_arr.append(TextSendMessage("以下提供給你所有球隊戰績"))
        content_arr.append(TextSendMessage("需要各別搜尋請輸入\n球隊名稱加上戰績"))
        content_arr.append(TextSendMessage("例如-勇士今年戰績-"))
        content_arr.append(TextSendMessage(GetAllTeamStandings()))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "補強建議":
        content_arr = []
        content_arr.append(TextSendMessage("請輸入球隊補強建議"))
        content_arr.append(TextSendMessage("例如:熱火補強建議"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "補強名單":
        content_arr = []
        content_arr.append(TextSendMessage("請輸入球隊補強名單"))
        content_arr.append(TextSendMessage("例如:熱火補強名單"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "問題":
        content_arr = []
        content_arr.append(TextSendMessage("可以喔，我能幫你解決所有籃球問題喔!"))
        content_arr.append(TextSendMessage("例如:賽程，球隊教練，球隊新聞等等"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0
    
    content_arr = []  # 初始化 content_arr 變數為空清單

    if text == "新聞":
        content_arr = UdnNews()

        # 创建消息数组，包括欢迎消息、说明消息和新闻标题消息
        content_arr.append(TextSendMessage("以下是最新十篇籃球新聞"))
        content_arr.append(TextSendMessage("需要各別搜尋請輸入球隊名稱加上新聞"))
        content_arr.append(TextSendMessage("例如-勇士新聞-"))

    if len(content_arr) > 5:
        content_arr = content_arr[:5]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0


    content_arr = []  # 初始化 content_arr 變數為空清單

    if text == "七六人新聞":
        content_arr = getaNews()
    # 將訊息數量限制在 5 個以內
    if len(content_arr) > 5:
        content_arr = content_arr[:5]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "76人新聞":
        content_arr = getaNews()
    # 將訊息數量限制在 5 個以內
    if len(content_arr) > 5:
        content_arr = content_arr[:5]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "公牛新聞":
        content_arr = getbNews()
    # 將訊息數量限制在 5 個以內
    if len(content_arr) > 5:
        content_arr = content_arr[:5]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "公鹿新聞":
        content_arr = getcNews()
    # 將訊息數量限制在 5 個以內
    if len(content_arr) > 5:
        content_arr = content_arr[:5]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "太陽新聞":
        content_arr = getdNews()
    # 將訊息數量限制在 5 個以內
    if len(content_arr) > 5:
        content_arr = content_arr[:5]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "火箭新聞":
        content_arr = geteNews()
    # 將訊息數量限制在 5 個以內
    if len(content_arr) > 5:
        content_arr = content_arr[:5]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "尼克新聞":
        content_arr = getfNews()
    # 將訊息數量限制在 5 個以內
    if len(content_arr) > 5:
        content_arr = content_arr[:5]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "灰狼新聞":
        content_arr = getgNews()
    # 將訊息數量限制在 5 個以內
    if len(content_arr) > 5:
        content_arr = content_arr[:5]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "灰熊新聞":
        content_arr = gethNews()
    # 將訊息數量限制在 5 個以內
    if len(content_arr) > 5:
        content_arr = content_arr[:5]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "老鷹新聞":
        content_arr = getiNews()
    # 將訊息數量限制在 5 個以內
    if len(content_arr) > 5:
        content_arr = content_arr[:5]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "巫師新聞":
        content_arr = getjNews()
    # 將訊息數量限制在 5 個以內
    if len(content_arr) > 5:
        content_arr = content_arr[:5]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "快艇新聞":
        content_arr = getkNews()
    # 將訊息數量限制在 5 個以內
    if len(content_arr) > 5:
        content_arr = content_arr[:5]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "拓荒者新聞":
        content_arr = getlNews()
    # 將訊息數量限制在 5 個以內
    if len(content_arr) > 5:
        content_arr = content_arr[:5]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "金塊新聞":
        content_arr = getmNews()
    # 將訊息數量限制在 5 個以內
    if len(content_arr) > 5:
        content_arr = content_arr[:5]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "勇士新聞":
        content_arr = getnNews()
    # 將訊息數量限制在 5 個以內
    if len(content_arr) > 5:
        content_arr = content_arr[:5]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "活塞新聞":
        content_arr = getoNews()
    # 將訊息數量限制在 5 個以內
    if len(content_arr) > 5:
        content_arr = content_arr[:5]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "馬刺新聞":
        content_arr = getpNews()
    # 將訊息數量限制在 5 個以內
    if len(content_arr) > 5:
        content_arr = content_arr[:5]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "國王新聞":
        content_arr = getqNews()
    # 將訊息數量限制在 5 個以內
    if len(content_arr) > 5:
        content_arr = content_arr[:5]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "湖人新聞":
        content_arr = getrNews()
    # 將訊息數量限制在 5 個以內
    if len(content_arr) > 5:
        content_arr = content_arr[:5]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "黃蜂新聞":
        content_arr = getxNews()
    # 將訊息數量限制在 5 個以內
    if len(content_arr) > 5:
        content_arr = content_arr[:5]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "塞爾提克新聞":
        content_arr = getyNews()
    # 將訊息數量限制在 5 個以內
    if len(content_arr) > 5:
        content_arr = content_arr[:5]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "溜馬新聞":
        content_arr = getzNews()
    # 將訊息數量限制在 5 個以內
    if len(content_arr) > 5:
        content_arr = content_arr[:5]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "雷霆新聞":
        content_arr = getaaNews()
    # 將訊息數量限制在 5 個以內
    if len(content_arr) > 5:
        content_arr = content_arr[:5]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "暴龍新聞":
        content_arr = getbbNews()
    # 將訊息數量限制在 5 個以內
    if len(content_arr) > 5:
        content_arr = content_arr[:5]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "熱火新聞":
        content_arr = getccNews()
    # 將訊息數量限制在 5 個以內
    if len(content_arr) > 5:
        content_arr = content_arr[:5]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "獨行俠新聞":
        content_arr = getddNews()
    # 將訊息數量限制在 5 個以內
    if len(content_arr) > 5:
        content_arr = content_arr[:5]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "爵士新聞":
        content_arr = geteeNews()
    # 將訊息數量限制在 5 個以內
    if len(content_arr) > 5:
        content_arr = content_arr[:5]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "騎士新聞":
        content_arr = getffNews()
    # 將訊息數量限制在 5 個以內
    if len(content_arr) > 5:
        content_arr = content_arr[:5]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "鵜鶘新聞":
        content_arr = getggNews()
    # 將訊息數量限制在 5 個以內
    if len(content_arr) > 5:
        content_arr = content_arr[:5]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "籃網新聞":
        content_arr = gethhNews()
    # 將訊息數量限制在 5 個以內
    if len(content_arr) > 5:
        content_arr = content_arr[:5]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "魔術新聞":
        content_arr = getiiNews()
    # 將訊息數量限制在 5 個以內
    if len(content_arr) > 5:
        content_arr = content_arr[:5]
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0
    
    if text == "巫師補強建議":  
            a01 = ["提供你巫師補強建議"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(巫師補強建議)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "黃蜂補強建議":  
            a01 = ["提供你黃蜂補強建議"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(黃蜂補強建議)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "老鷹補強建議":  
            a01 = ["提供你老鷹補強建議"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(老鷹補強建議)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "熱火補強建議":  
            a01 = ["提供你熱火補強建議"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(熱火補強建議)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "魔術補強建議":  
            a01 = ["提供你魔術補強建議"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(魔術補強建議)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "尼克補強建議":  
            a01 = ["提供你尼克補強建議"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(尼克補強建議)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "76人補強建議":  
            a01 = ["提供你76人補強建議"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(七六人補強建議)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "七六人補強建議":  
            a01 = ["提供你七六人補強建議"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(七六人補強建議)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "籃網補強建議":  
            a01 = ["提供你籃網補強建議"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(籃網補強建議)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "塞爾提克補強建議":  
            a01 = ["提供你塞爾提克補強建議"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(塞爾提克補強建議)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "暴龍補強建議":  
            a01 = ["提供你暴龍補強建議"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(暴龍補強建議)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "公牛補強建議":  
            a01 = ["提供你公牛補強建議"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(公牛補強建議)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "騎士補強建議":  
            a01 = ["提供你騎士補強建議"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(騎士補強建議)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "溜馬補強建議":  
            a01 = ["提供你溜馬補強建議"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(溜馬補強建議)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "活塞補強建議":  
            a01 = ["提供你活塞補強建議"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(活塞補強建議)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "公鹿補強建議":  
            a01 = ["提供你公鹿補強建議"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(公鹿補強建議)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "灰狼補強建議":  
            a01 = ["提供你灰狼補強建議"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(灰狼補強建議)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "爵士補強建議":  
            a01 = ["提供你爵士補強建議"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(爵士補強建議)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "雷霆補強建議":  
            a01 = ["提供你雷霆補強建議"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(雷霆補強建議)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "拓荒者補強建議":  
            a01 = ["提供你拓荒者補強建議"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(拓荒者補強建議)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "金塊補強建議":  
            a01 = ["提供你金塊補強建議"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(金塊補強建議)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "灰熊補強建議":  
            a01 = ["提供你灰熊補強建議"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(灰熊補強建議)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "火箭補強建議":  
            a01 = ["提供你火箭補強建議"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(火箭補強建議)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "鵜鶘補強建議":  
            a01 = ["提供你鵜鶘補強建議"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(鵜鶘補強建議)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "馬刺補強建議":  
            a01 = ["提供你馬刺補強建議"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(馬刺補強建議)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "獨行俠補強建議":  
            a01 = ["提供你獨行俠補強建議"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(獨行俠補強建議)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "勇士補強建議":  
            a01 = ["提供你勇士補強建議"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(勇士補強建議)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "湖人補強建議":  
            a01 = ["提供你湖人補強建議"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(湖人補強建議)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "快艇補強建議":  
            a01 = ["提供你快艇補強建議"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(快艇補強建議)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "太陽補強建議":  
            a01 = ["提供你太陽補強建議"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(太陽補強建議)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "國王補強建議":  
            a01 = ["提供你國王補強建議"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(國王補強建議)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0

    if text == "補強建議":  
            content_arr.append(TextSendMessage(random_statement(補強建議)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0

    if text == "巫師補強名單":  
            a01 = ["提供你巫師補強名單"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(巫師補強名單)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    #if text == "黃蜂補強名單":  
            #a01 = ["提供你黃蜂補強名單"]
            #content_arr = []
            #content_arr.append(TextSendMessage(random_statement(a01)))
            #content_arr.append(TextSendMessage(random_statement(黃蜂補強名單)))
            #line_bot_api.reply_message(event.reply_token, content_arr)
            #return 0
    if text == "老鷹補強名單":  
            a01 = ["提供你老鷹補強名單"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(老鷹補強名單)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "熱火補強名單":  
            a01 = ["提供你熱火補強名單"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(熱火補強名單)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "魔術補強名單":  
            a01 = ["提供你魔術補強名單"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(魔術補強名單)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "尼克補強名單":  
            a01 = ["提供你尼克補強名單"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(尼克補強名單)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "76人補強名單":  
            a01 = ["提供你76人補強名單"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(七六人補強名單)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "七六人補強名單":  
            a01 = ["提供你七六人補強名單"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(七六人補強名單)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "籃網補強名單":  
            a01 = ["提供你籃網補強名單"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(籃網補強名單)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "塞爾提克補強名單":  
            a01 = ["提供你塞爾提克補強名單"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(塞爾提克補強名單)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "暴龍補強名單":  
            a01 = ["提供你暴龍補強名單"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(暴龍補強名單)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "公牛補強名單":  
            a01 = ["提供你公牛補強名單"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(公牛補強名單)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "騎士補強名單":  
            a01 = ["提供你騎士補強名單"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(騎士補強名單)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "溜馬補強名單":  
            a01 = ["提供你溜馬補強名單"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(溜馬補強名單)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "活塞補強名單":  
            a01 = ["提供你活塞補強名單"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(活塞補強名單)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "公鹿補強名單":  
            a01 = ["提供你公鹿補強名單"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(公鹿補強名單)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "灰狼補強名單":  
            a01 = ["提供你灰狼補強名單"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(灰狼補強名單)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "爵士補強名單":  
            a01 = ["提供你爵士補強名單"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(爵士補強名單)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "雷霆補強名單":  
            a01 = ["提供你雷霆補強名單"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(雷霆補強名單)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "拓荒者補強名單":  
            a01 = ["提供你拓荒者補強名單"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(拓荒者補強名單)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "金塊補強名單":  
            a01 = ["提供你金塊補強名單"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(金塊補強名單)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "灰熊補強名單":  
            a01 = ["提供你灰熊補強名單"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(灰熊補強名單)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "":  
            a01 = ["提供你"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement()))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "火箭補強名單":  
            a01 = ["提供你火箭補強名單"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(火箭補強名單)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "鵜鶘補強名單":  
            a01 = ["提供你鵜鶘補強名單"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(鵜鶘補強名單)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "馬刺補強名單":  
            a01 = ["提供你馬刺補強名單"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(馬刺補強名單)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "獨行俠補強名單":  
            a01 = ["提供你獨行俠補強名單"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(獨行俠補強名單)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "勇士補強名單":  
            a01 = ["提供你勇士補強名單"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(勇士補強名單)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "湖人補強名單":  
            a01 = ["提供你湖人補強名單"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(湖人補強名單)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "快艇補強名單":  
            a01 = ["提供你快艇補強名單"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(快艇補強名單)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "太陽補強名單":  
            a01 = ["提供你太陽補強名單"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(太陽補強名單)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "國王補強名單":  
            a01 = ["提供你國王補強名單"]
            content_arr = []
            content_arr.append(TextSendMessage(random_statement(a01)))
            content_arr.append(TextSendMessage(random_statement(國王補強名單)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "補強名單":  
            content_arr.append(TextSendMessage(random_statement(補強名單)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0    
    if text == "巫師去年排名":  
            content_arr.append(TextSendMessage(random_statement(巫師去年排名)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "黃蜂去年排名":  
            content_arr.append(TextSendMessage(random_statement(黃蜂去年排名)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "老鷹去年排名":  
            content_arr.append(TextSendMessage(random_statement(老鷹去年排名)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "熱火去年排名":  
            content_arr.append(TextSendMessage(random_statement(熱火去年排名)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "魔術去年排名":  
            content_arr.append(TextSendMessage(random_statement(魔術去年排名)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "尼克去年排名":  
            content_arr.append(TextSendMessage(random_statement(尼克去年排名)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "76人去年排名":  
            content_arr.append(TextSendMessage(random_statement(七六人去年排名)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "七六人去年排名":  
            content_arr.append(TextSendMessage(random_statement(七六人去年排名)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "籃網去年排名":  
            content_arr.append(TextSendMessage(random_statement(籃網去年排名)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "塞爾提克去年排名":  
            content_arr.append(TextSendMessage(random_statement(塞爾提克去年排名)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "暴龍去年排名":  
            content_arr.append(TextSendMessage(random_statement(暴龍去年排名)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "公牛去年排名":  
            content_arr.append(TextSendMessage(random_statement(公牛去年排名)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "騎士去年排名":  
            content_arr.append(TextSendMessage(random_statement(騎士去年排名)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "溜馬去年排名":  
            content_arr.append(TextSendMessage(random_statement(溜馬去年排名)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "活塞去年排名":  
            content_arr.append(TextSendMessage(random_statement(活塞去年排名)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "灰狼去年排名":  
            content_arr.append(TextSendMessage(random_statement(灰狼去年排名)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "爵士去年排名":  
            content_arr.append(TextSendMessage(random_statement(爵士去年排名)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "雷霆去年排名":  
            content_arr.append(TextSendMessage(random_statement(雷霆去年排名)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "拓荒者去年排名":  
            content_arr.append(TextSendMessage(random_statement(拓荒者去年排名)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "金塊去年排名":  
            content_arr.append(TextSendMessage(random_statement(金塊去年排名)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "灰熊去年排名":  
            content_arr.append(TextSendMessage(random_statement(灰熊去年排名)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "火箭去年排名":  
            content_arr.append(TextSendMessage(random_statement(火箭去年排名)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "鵜鶘去年排名":  
            content_arr.append(TextSendMessage(random_statement(鵜鶘去年排名)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "馬刺去年排名":  
            content_arr.append(TextSendMessage(random_statement(馬刺去年排名)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "獨行俠去年排名":  
            content_arr.append(TextSendMessage(random_statement(獨行俠去年排名)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "勇士去年排名":  
            content_arr.append(TextSendMessage(random_statement(勇士去年排名)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "湖人去年排名":  
            content_arr.append(TextSendMessage(random_statement(湖人去年排名)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "快艇去年排名":  
            content_arr.append(TextSendMessage(random_statement(快艇去年排名)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "太陽去年排名":  
            content_arr.append(TextSendMessage(random_statement(太陽去年排名)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "國王去年排名":  
            content_arr.append(TextSendMessage(random_statement(國王去年排名)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0    



   
    if text == "巫師去年戰績":  
            content_arr.append(TextSendMessage(random_statement(巫師去年戰績)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "黃蜂去年戰績":  
            content_arr.append(TextSendMessage(random_statement(黃蜂去年戰績)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "老鷹去年戰績":  
            content_arr.append(TextSendMessage(random_statement(老鷹去年戰績)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "熱火去年戰績":  
            content_arr.append(TextSendMessage(random_statement(熱火去年戰績)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "魔術去年戰績":  
            content_arr.append(TextSendMessage(random_statement(魔術去年戰績)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "尼克去年戰績":  
            content_arr.append(TextSendMessage(random_statement(尼克去年戰績)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "76人去年戰績":  
            content_arr.append(TextSendMessage(random_statement(七六人去年戰績)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "七六人去年戰績":  
            content_arr.append(TextSendMessage(random_statement(七六人去年戰績)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "籃網去年戰績":  
            content_arr.append(TextSendMessage(random_statement(籃網去年戰績)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "塞爾提克去年戰績":  
            content_arr.append(TextSendMessage(random_statement(塞爾提克去年戰績)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "暴龍去年戰績":  
            content_arr.append(TextSendMessage(random_statement(暴龍去年戰績)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "公牛去年戰績":  
            content_arr.append(TextSendMessage(random_statement(公牛去年戰績)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "騎士去年戰績":  
            content_arr.append(TextSendMessage(random_statement(騎士去年戰績)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "溜馬去年戰績":  
            content_arr.append(TextSendMessage(random_statement(溜馬去年戰績)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "活塞去年戰績":  
            content_arr.append(TextSendMessage(random_statement(活塞去年戰績)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "灰狼去年戰績":  
            content_arr.append(TextSendMessage(random_statement(灰狼去年戰績)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "爵士去年戰績":  
            content_arr.append(TextSendMessage(random_statement(爵士去年戰績)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "雷霆去年戰績":  
            content_arr.append(TextSendMessage(random_statement(雷霆去年戰績)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "拓荒者去年戰績":  
            content_arr.append(TextSendMessage(random_statement(拓荒者去年戰績)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "金塊去年戰績":  
            content_arr.append(TextSendMessage(random_statement(金塊去年戰績)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "灰熊去年戰績":  
            content_arr.append(TextSendMessage(random_statement(灰熊去年戰績)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "火箭去年戰績":  
            content_arr.append(TextSendMessage(random_statement(火箭去年戰績)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "鵜鶘去年戰績排名":  
            content_arr.append(TextSendMessage(random_statement(鵜鶘去年戰績)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "馬刺去年戰績":  
            content_arr.append(TextSendMessage(random_statement(馬刺去年戰績)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "獨行俠去年戰績":  
            content_arr.append(TextSendMessage(random_statement(獨行俠去年戰績)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "勇士去年戰績":  
            content_arr.append(TextSendMessage(random_statement(勇士去年戰績)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "湖人去年戰績":  
            content_arr.append(TextSendMessage(random_statement(湖人去年戰績)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "快艇去年戰績":  
            content_arr.append(TextSendMessage(random_statement(快艇去年戰績)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "太陽去年戰績":  
            content_arr.append(TextSendMessage(random_statement(太陽去年戰績)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0   
    if text == "國王去年戰績":  
            content_arr.append(TextSendMessage(random_statement(國王去年戰績)))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0 



    if text == "老鷹十月賽程":
        team_code = "hawks"  # 代碼
        month = 10
        hawks_schedule = GetAllTeamSchedules(team_code, month)  # 使用上一個回答中的函數

        if hawks_schedule:
            messages = hawks_schedule.get("老鷹")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"老鷹{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "老鷹十一月賽程":
        team_code = "hawks"  # 代碼
        month = 11
        hawks_schedule = GetAllTeamSchedules(team_code, month)

        if hawks_schedule:
            messages = hawks_schedule.get("老鷹")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"老鷹{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "老鷹十二月賽程":
        team_code = "hawks"  # 代碼
        month = 12
        hawks_schedule = GetAllTeamSchedules(team_code, month)

        if hawks_schedule:
            messages = hawks_schedule.get("老鷹")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"老鷹{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "老鷹一月賽程":
        team_code = "hawks"  # 代碼
        month = 1
        hawks_schedule = GetAllTeamSchedules(team_code, month)

        if hawks_schedule:
            messages = hawks_schedule.get("老鷹")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"老鷹{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "老鷹二月賽程":
        team_code = "hawks"  # 代碼
        month = 2
        hawks_schedule = GetAllTeamSchedules(team_code, month)

        if hawks_schedule:
            messages = hawks_schedule.get("老鷹")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"老鷹{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "老鷹三月賽程":
        team_code = "hawks"  # 代碼
        month = 3
        hawks_schedule = GetAllTeamSchedules(team_code, month)

        if hawks_schedule:
            messages = hawks_schedule.get("老鷹")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"老鷹{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "老鷹四月賽程":
        team_code = "hawks"  # 代碼
        month = 4
        hawks_schedule = GetAllTeamSchedules(team_code, month)

        if hawks_schedule:
            messages = hawks_schedule.get("老鷹")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"老鷹{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "塞爾提克十月賽程":
        team_code = "celtics"  # 代碼
        month = 10
        celtics_schedule = GetAllTeamSchedules(team_code, month)

        if celtics_schedule:
            messages = celtics_schedule.get("凱爾特人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"凱爾特人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "塞爾提克十一月賽程":
        team_code = "celtics"  # 代碼
        month = 11
        celtics_schedule = GetAllTeamSchedules(team_code, month)
        if celtics_schedule:
            messages = celtics_schedule.get("凱爾特人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"凱爾特人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "塞爾提克十二月賽程":
        team_code = "celtics"  # 代碼
        month = 12
        celtics_schedule = GetAllTeamSchedules(team_code, month)

        if celtics_schedule:
            messages = celtics_schedule.get("凱爾特人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"凱爾特人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "塞爾提克一月賽程":
        team_code = "celtics"  # 代碼
        month = 1
        celtics_schedule = GetAllTeamSchedules(team_code, month)

        if celtics_schedule:
            messages = celtics_schedule.get("凱爾特人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"凱爾特人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "塞爾提克二月賽程":
        team_code = "celtics"  # 代碼
        month = 2
        celtics_schedule = GetAllTeamSchedules(team_code, month)

        if celtics_schedule:
            messages = celtics_schedule.get("凱爾特人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"凱爾特人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "塞爾提克三月賽程":
        team_code = "celtics"  # 代碼
        month = 3
        celtics_schedule = GetAllTeamSchedules(team_code, month)

        if celtics_schedule:
            messages = celtics_schedule.get("凱爾特人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"凱爾特人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "塞爾提克四月賽程":
        team_code = "celtics"  # 代碼
        month = 4
        celtics_schedule = GetAllTeamSchedules(team_code, month)

        if celtics_schedule:
            messages = celtics_schedule.get("凱爾特人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"凱爾特人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "公牛十月賽程":
        team_code = "bulls"  # 代碼
        month = 10
        bulls_schedule = GetAllTeamSchedules(team_code, month)

        if bulls_schedule:
            messages = bulls_schedule.get("公牛")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"公牛{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "公牛十一月賽程":
        team_code = "bulls"  # 代碼
        month = 11
        bulls_schedule = GetAllTeamSchedules(team_code, month)

        if bulls_schedule:
            messages = bulls_schedule.get("公牛")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"公牛{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "公牛十二月賽程":
        team_code = "bulls"  # 代碼
        month = 12
        bulls_schedule = GetAllTeamSchedules(team_code, month)

        if bulls_schedule:
            messages = bulls_schedule.get("公牛")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"公牛{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "公牛一月賽程":
        team_code = "bulls"  # 代碼
        month = 1
        bulls_schedule = GetAllTeamSchedules(team_code, month)

        if bulls_schedule:
            messages = bulls_schedule.get("公牛")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"公牛{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "公牛二月賽程":
        team_code = "bulls"  # 代碼
        month = 2
        bulls_schedule = GetAllTeamSchedules(team_code, month)

        if bulls_schedule:
            messages = bulls_schedule.get("公牛")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"公牛{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "公牛三月賽程":
        team_code = "bulls"  # 代碼
        month = 3
        bulls_schedule = GetAllTeamSchedules(team_code, month)

        if bulls_schedule:
            messages = bulls_schedule.get("公牛")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"公牛{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "公牛四月賽程":
        team_code = "bulls"  # 代碼
        month = 4
        bulls_schedule = GetAllTeamSchedules(team_code, month)

        if bulls_schedule:
            messages = bulls_schedule.get("公牛")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"公牛{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "黃蜂十月賽程":
        team_code = "hornets"  # 代碼
        month = 10
        hornets_schedule = GetAllTeamSchedules(team_code, month)

        if hornets_schedule:
            messages = hornets_schedule.get("黃蜂")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"黃蜂{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "黃蜂十一月賽程":
        team_code = "hornets"  # 代碼
        month = 11
        hornets_schedule = GetAllTeamSchedules(team_code, month)

        if hornets_schedule:
            messages = hornets_schedule.get("黃蜂")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"黃蜂{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "黃蜂十二月賽程":
        team_code = "hornets"  # 代碼
        month = 12
        hornets_schedule = GetAllTeamSchedules(team_code, month)

        if hornets_schedule:
            messages = hornets_schedule.get("黃蜂")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"黃蜂{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "黃蜂一月賽程":
        team_code = "hornets"  # 代碼
        month = 1
        hornets_schedule = GetAllTeamSchedules(team_code, month)

        if hornets_schedule:
            messages = hornets_schedule.get("黃蜂")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"黃蜂{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "黃蜂二月賽程":
        team_code = "hornets"  # 代碼
        month = 2
        hornets_schedule = GetAllTeamSchedules(team_code, month)
        if hornets_schedule:
            messages = hornets_schedule.get("黃蜂")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"黃蜂{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "黃蜂三月賽程":
        team_code = "hornets"  # 代碼
        month = 3
        hornets_schedule = GetAllTeamSchedules(team_code, month)

        if hornets_schedule:
            messages = hornets_schedule.get("黃蜂")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"黃蜂{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "黃蜂四月賽程":
        team_code = "hornets"  # 代碼
        month = 4
        hornets_schedule = GetAllTeamSchedules(team_code, month)

        if hornets_schedule:
            messages = hornets_schedule.get("黃蜂")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"黃蜂{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "籃網十月賽程":
        team_code = "nets"  # 代碼
        month = 10
        nets_schedule = GetAllTeamSchedules(team_code, month)

        if nets_schedule:
            messages = nets_schedule.get("籃網")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"籃網{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "籃網十一月賽程":
        team_code = "nets"  # 代碼
        month = 11
        nets_schedule = GetAllTeamSchedules(team_code, month)

        if nets_schedule:
            messages = nets_schedule.get("籃網")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"籃網{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "籃網十二月賽程":
        team_code = "nets"  # 代碼
        month = 12
        nets_schedule = GetAllTeamSchedules(team_code, month)

        if nets_schedule:
            messages = nets_schedule.get("籃網")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"籃網{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "籃網一月賽程":
        team_code = "nets"  # 代碼
        month = 1
        nets_schedule = GetAllTeamSchedules(team_code, month)

        if nets_schedule:
            messages = nets_schedule.get("籃網")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"籃網{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "籃網二月賽程":
        team_code = "nets"  # 代碼
        month = 2
        nets_schedule = GetAllTeamSchedules(team_code, month)

        if nets_schedule:
            messages = nets_schedule.get("籃網")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"籃網{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "籃網三月賽程":
        team_code = "nets"  # 代碼
        month = 3
        nets_schedule = GetAllTeamSchedules(team_code, month)

        if nets_schedule:
            messages = nets_schedule.get("籃網")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"籃網{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "籃網四月賽程":
        team_code = "nets"  # 代碼
        month = 4
        nets_schedule = GetAllTeamSchedules(team_code, month)

        if nets_schedule:
            messages = nets_schedule.get("籃網")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"籃網{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "騎士十月賽程":
        team_code = "cavaliers"  # 代碼
        month = 10
        cavaliers_schedule = GetAllTeamSchedules(team_code, month)

        if cavaliers_schedule:
            messages = cavaliers_schedule.get("騎士")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"騎士{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "騎士十一月賽程":
        team_code = "cavaliers"  # 代碼
        month = 11
        cavaliers_schedule = GetAllTeamSchedules(team_code, month)

        if cavaliers_schedule:
            messages = cavaliers_schedule.get("騎士")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"騎士{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "騎士十二月賽程":
        team_code = "cavaliers"  # 代碼
        month = 12
        cavaliers_schedule = GetAllTeamSchedules(team_code, month)

        if cavaliers_schedule:
            messages = cavaliers_schedule.get("騎士")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"騎士{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "騎士一月賽程":
        team_code = "cavaliers"  # 代碼
        month = 1
        cavaliers_schedule = GetAllTeamSchedules(team_code, month)

        if cavaliers_schedule:
            messages = cavaliers_schedule.get("騎士")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"騎士{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "騎士二月賽程":
        team_code = "cavaliers"  # 代碼
        month = 2
        cavaliers_schedule = GetAllTeamSchedules(team_code, month)

        if cavaliers_schedule:
            messages = cavaliers_schedule.get("騎士")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"騎士{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "騎士三月賽程":
        team_code = "cavaliers"  # 代碼
        month = 3
        cavaliers_schedule = GetAllTeamSchedules(team_code, month)

        if cavaliers_schedule:
            messages = cavaliers_schedule.get("騎士")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"騎士{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "騎士四月賽程":
        team_code = "cavaliers"  # 代碼
        month = 4
        cavaliers_schedule = GetAllTeamSchedules(team_code, month)

        if cavaliers_schedule:
            messages = cavaliers_schedule.get("騎士")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"騎士{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "熱火十月賽程":
        team_code = "heat"  # 代碼
        month = 10
        heat_schedule = GetAllTeamSchedules(team_code, month)

        if heat_schedule:
            messages = heat_schedule.get("熱火")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"熱火{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "熱火十一月賽程":
        team_code = "heat"  # 代碼
        month = 11
        heat_schedule = GetAllTeamSchedules(team_code, month)

        if heat_schedule:
            messages = heat_schedule.get("熱火")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"熱火{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "熱火十二月賽程":
        team_code = "heat"  # 代碼
        month = 12
        heat_schedule = GetAllTeamSchedules(team_code, month)

        if heat_schedule:
            messages = heat_schedule.get("熱火")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"熱火{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "熱火一月賽程":
        team_code = "heat"  # 代碼
        month = 1
        heat_schedule = GetAllTeamSchedules(team_code, month)

        if heat_schedule:
            messages = heat_schedule.get("熱火")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"熱火{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "熱火二月賽程":
        team_code = "heat"  # 代碼
        month = 2
        heat_schedule = GetAllTeamSchedules(team_code, month)

        if heat_schedule:
            messages = heat_schedule.get("熱火")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"熱火{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "熱火三月賽程":
        team_code = "heat"  # 代碼
        month = 3
        heat_schedule = GetAllTeamSchedules(team_code, month)

        if heat_schedule:
            messages = heat_schedule.get("熱火")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"熱火{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "熱火四月賽程":
        team_code = "heat"  # 代碼
        month = 4
        heat_schedule = GetAllTeamSchedules(team_code, month)

        if heat_schedule:
            messages = heat_schedule.get("熱火")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"熱火{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "尼克十月賽程":
        team_code = "knicks"  # 代碼
        month = 10
        knicks_schedule = GetAllTeamSchedules(team_code, month)

        if knicks_schedule:
            messages = knicks_schedule.get("尼克斯")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"尼克斯{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "尼克十一月賽程":
        team_code = "knicks"  # 代碼
        month = 11
        knicks_schedule = GetAllTeamSchedules(team_code, month)

        if knicks_schedule:
            messages = knicks_schedule.get("尼克斯")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"尼克斯{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "尼克十二月賽程":
        team_code = "knicks"  # 代碼
        month = 12
        knicks_schedule = GetAllTeamSchedules(team_code, month)

        if knicks_schedule:
            messages = knicks_schedule.get("尼克斯")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"尼克斯{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "尼克一月賽程":
        team_code = "knicks"  # 代碼
        month = 1
        knicks_schedule = GetAllTeamSchedules(team_code, month)

        if knicks_schedule:
            messages = knicks_schedule.get("尼克斯")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"尼克斯{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "尼克二月賽程":
        team_code = "knicks"  # 代碼
        month = 2
        knicks_schedule = GetAllTeamSchedules(team_code, month)

        if knicks_schedule:
            messages = knicks_schedule.get("尼克斯")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"尼克斯{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "尼克三月賽程":
        team_code = "knicks"  # 代碼
        month = 3
        knicks_schedule = GetAllTeamSchedules(team_code, month)

        if knicks_schedule:
            messages = knicks_schedule.get("尼克斯")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"尼克斯{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "尼克四月賽程":
        team_code = "knicks"  # 代碼
        month = 4
        knicks_schedule = GetAllTeamSchedules(team_code, month)

        if knicks_schedule:
            messages = knicks_schedule.get("尼克斯")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"尼克斯{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "活塞十月賽程":
        team_code = "pistons"  # 代碼
        month = 10
        pistons_schedule = GetAllTeamSchedules(team_code, month)

        if pistons_schedule:
            messages = pistons_schedule.get("活塞")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"活塞{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "活塞十一月賽程":
        team_code = "pistons"  # 代碼
        month = 11
        pistons_schedule = GetAllTeamSchedules(team_code, month)

        if pistons_schedule:
            messages = pistons_schedule.get("活塞")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"活塞{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "活塞十二月賽程":
        team_code = "pistons"  # 代碼
        month = 12
        pistons_schedule = GetAllTeamSchedules(team_code, month)

        if pistons_schedule:
            messages = pistons_schedule.get("活塞")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"活塞{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "活塞一月賽程":
        team_code = "pistons"  # 代碼
        month = 1
        pistons_schedule = GetAllTeamSchedules(team_code, month)

        if pistons_schedule:
            messages = pistons_schedule.get("活塞")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"活塞{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "活塞二月賽程":
        team_code = "pistons"  # 代碼
        month = 2
        pistons_schedule = GetAllTeamSchedules(team_code, month)

        if pistons_schedule:
            messages = pistons_schedule.get("活塞")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"活塞{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "活塞三月賽程":
        team_code = "pistons"  # 代碼
        month = 3
        pistons_schedule = GetAllTeamSchedules(team_code, month)

        if pistons_schedule:
            messages = pistons_schedule.get("活塞")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"活塞{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "活塞四月賽程":
        team_code = "pistons"  # 代碼
        month = 4
        pistons_schedule = GetAllTeamSchedules(team_code, month)

        if pistons_schedule:
            messages = pistons_schedule.get("活塞")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"活塞{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "魔術十月賽程":
        team_code = "magic"  # 代碼
        month = 10
        magic_schedule = GetAllTeamSchedules(team_code, month)

        if magic_schedule:
            messages = magic_schedule.get("魔術")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"魔術{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "魔術十一月賽程":
        team_code = "magic"  # 代碼
        month = 11
        magic_schedule = GetAllTeamSchedules(team_code, month)

        if magic_schedule:
            messages = magic_schedule.get("魔術")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"魔術{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "魔術十二月賽程":
        team_code = "magic"  # 代碼
        month = 12
        magic_schedule = GetAllTeamSchedules(team_code, month)

        if magic_schedule:
            messages = magic_schedule.get("魔術")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"魔術{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "魔術一月賽程":
        team_code = "magic"  # 代碼
        month = 1
        magic_schedule = GetAllTeamSchedules(team_code, month)

        if magic_schedule:
            messages = magic_schedule.get("魔術")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"魔術{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "魔術二月賽程":
        team_code = "magic"  # 代碼
        month = 2
        magic_schedule = GetAllTeamSchedules(team_code, month)

        if magic_schedule:
            messages = magic_schedule.get("魔術")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"魔術{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "魔術三月賽程":
        team_code = "magic"  # 代碼
        month = 3
        magic_schedule = GetAllTeamSchedules(team_code, month)

        if magic_schedule:
            messages = magic_schedule.get("魔術")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"魔術{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "魔術四月賽程":
        team_code = "magic"  # 代碼
        month = 4
        magic_schedule = GetAllTeamSchedules(team_code, month)

        if magic_schedule:
            messages = magic_schedule.get("魔術")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"魔術{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "溜馬十月賽程":
        team_code = "pacers"  # 代碼
        month = 10
        pacers_schedule = GetAllTeamSchedules(team_code, month)

        if pacers_schedule:
            messages = pacers_schedule.get("步行者")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"步行者{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "溜馬十一月賽程":
        team_code = "pacers"  # 代碼
        month = 11
        pacers_schedule = GetAllTeamSchedules(team_code, month)

        if pacers_schedule:
            messages = pacers_schedule.get("步行者")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"步行者{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "溜馬十二月賽程":
        team_code = "pacers"  # 代碼
        month = 12
        pacers_schedule = GetAllTeamSchedules(team_code, month)

        if pacers_schedule:
            messages = pacers_schedule.get("步行者")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"步行者{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "溜馬一月賽程":
        team_code = "pacers"  # 代碼
        month = 1
        pacers_schedule = GetAllTeamSchedules(team_code, month)

        if pacers_schedule:
            messages = pacers_schedule.get("步行者")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"步行者{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "溜馬二月賽程":
        team_code = "pacers"  # 代碼
        month = 2
        pacers_schedule = GetAllTeamSchedules(team_code, month)

        if pacers_schedule:
            messages = pacers_schedule.get("步行者")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"步行者{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "溜馬三月賽程":
        team_code = "pacers"  # 代碼
        month = 3
        pacers_schedule = GetAllTeamSchedules(team_code, month)

        if pacers_schedule:
            messages = pacers_schedule.get("步行者")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"步行者{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "溜馬四月賽程":
        team_code = "pacers"  # 代碼
        month = 4
        pacers_schedule = GetAllTeamSchedules(team_code, month)

        if pacers_schedule:
            messages = pacers_schedule.get("步行者")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"步行者{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "巫師十月賽程":
        team_code = "wizards"  # 代碼
        month = 10
        wizards_schedule = GetAllTeamSchedules(team_code, month)

        if wizards_schedule:
            messages = wizards_schedule.get("奇才")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"奇才{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "巫師十一月賽程":
        team_code = "wizards"  # 代碼
        month = 11
        wizards_schedule = GetAllTeamSchedules(team_code, month)

        if wizards_schedule:
            messages = wizards_schedule.get("奇才")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"奇才{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "巫師十二月賽程":
        team_code = "wizards"  # 代碼
        month = 12
        wizards_schedule = GetAllTeamSchedules(team_code, month)

        if wizards_schedule:
            messages = wizards_schedule.get("奇才")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"奇才{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "巫師一月賽程":
        team_code = "wizards"  # 代碼
        month = 1
        wizards_schedule = GetAllTeamSchedules(team_code, month)

        if wizards_schedule:
            messages = wizards_schedule.get("奇才")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"奇才{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "巫師二月賽程":
        team_code = "wizards"  # 代碼
        month = 2
        wizards_schedule = GetAllTeamSchedules(team_code, month)

        if wizards_schedule:
            messages = wizards_schedule.get("奇才")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"奇才{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "巫師三月賽程":
        team_code = "wizards"  # 代碼
        month = 3
        wizards_schedule = GetAllTeamSchedules(team_code, month)

        if wizards_schedule:
            messages = wizards_schedule.get("奇才")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"奇才{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "巫師四月賽程":
        team_code = "wizards"  # 代碼
        month = 4
        wizards_schedule = GetAllTeamSchedules(team_code, month)

        if wizards_schedule:
            messages = wizards_schedule.get("奇才")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"奇才{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "暴龍十月賽程":
        team_code = "raptors"  # 代碼
        month = 10
        raptors_schedule = GetAllTeamSchedules(team_code, month)

        if raptors_schedule:
            messages = raptors_schedule.get("猛龍")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"猛龍{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "暴龍十一月賽程":
        team_code = "raptors"  # 代碼
        month = 11
        raptors_schedule = GetAllTeamSchedules(team_code, month)

        if raptors_schedule:
            messages = raptors_schedule.get("猛龍")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"猛龍{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "暴龍十二月賽程":
        team_code = "raptors"  # 代碼
        month = 12
        raptors_schedule = GetAllTeamSchedules(team_code, month)

        if raptors_schedule:
            messages = raptors_schedule.get("猛龍")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"猛龍{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "暴龍一月賽程":
        team_code = "raptors"  # 代碼
        month = 1
        raptors_schedule = GetAllTeamSchedules(team_code, month)

        if raptors_schedule:
            messages = raptors_schedule.get("猛龍")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"猛龍{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "暴龍二月賽程":
        team_code = "raptors"  # 代碼
        month = 2
        raptors_schedule = GetAllTeamSchedules(team_code, month)

        if raptors_schedule:
            messages = raptors_schedule.get("猛龍")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"猛龍{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "暴龍三月賽程":
        team_code = "raptors"  # 代碼
        month = 3
        raptors_schedule = GetAllTeamSchedules(team_code, month)

        if raptors_schedule:
            messages = raptors_schedule.get("猛龍")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"猛龍{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "暴龍四月賽程":
        team_code = "raptors"  # 代碼
        month = 4
        raptors_schedule = GetAllTeamSchedules(team_code, month)

        if raptors_schedule:
            messages = raptors_schedule.get("猛龍")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"猛龍{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "公鹿十月賽程":
        team_code = "bucks"  # 代碼
        month = 10
        bucks_schedule = GetAllTeamSchedules(team_code, month)

        if bucks_schedule:
            messages = bucks_schedule.get("雄鹿")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"雄鹿{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "公鹿十一月賽程":
        team_code = "bucks"  # 代碼
        month = 11
        bucks_schedule = GetAllTeamSchedules(team_code, month)

        if bucks_schedule:
            messages = bucks_schedule.get("雄鹿")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"雄鹿{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "公鹿十二月賽程":
        team_code = "bucks"  # 代碼
        month = 12
        bucks_schedule = GetAllTeamSchedules(team_code, month)

        if bucks_schedule:
            messages = bucks_schedule.get("雄鹿")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"雄鹿{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "公鹿一月賽程":
        team_code = "bucks"  # 代碼
        month = 1
        bucks_schedule = GetAllTeamSchedules(team_code, month)

        if bucks_schedule:
            messages = bucks_schedule.get("雄鹿")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"雄鹿{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "公鹿二月賽程":
        team_code = "bucks"  # 代碼
        month = 2
        bucks_schedule = GetAllTeamSchedules(team_code, month)

        if bucks_schedule:
            messages = bucks_schedule.get("雄鹿")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"雄鹿{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "公鹿三月賽程":
        team_code = "bucks"  # 代碼
        month = 3
        bucks_schedule = GetAllTeamSchedules(team_code, month)

        if bucks_schedule:
            messages = bucks_schedule.get("雄鹿")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"雄鹿{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "公鹿四月賽程":
        team_code = "bucks"  # 代碼
        month = 4
        bucks_schedule = GetAllTeamSchedules(team_code, month)

        if bucks_schedule:
            messages = bucks_schedule.get("雄鹿")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"雄鹿{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "獨行俠十月賽程":
        team_code = "mavericks"  # 代碼
        month = 10
        mavericks_schedule = GetAllTeamSchedules(team_code, month)

        if mavericks_schedule:
            messages = mavericks_schedule.get("獨行俠")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"獨行俠{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "獨行俠十一月賽程":
        team_code = "mavericks"  # 代碼
        month = 11
        mavericks_schedule = GetAllTeamSchedules(team_code, month)

        if mavericks_schedule:
            messages = mavericks_schedule.get("獨行俠")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"獨行俠{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "獨行俠十二月賽程":
        team_code = "mavericks"  # 代碼
        month = 12
        mavericks_schedule = GetAllTeamSchedules(team_code, month)

        if mavericks_schedule:
            messages = mavericks_schedule.get("獨行俠")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"獨行俠{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "獨行俠一月賽程":
        team_code = "mavericks"  # 代碼
        month = 1
        mavericks_schedule = GetAllTeamSchedules(team_code, month)

        if mavericks_schedule:
            messages = mavericks_schedule.get("獨行俠")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"獨行俠{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "獨行俠二月賽程":
        team_code = "mavericks"  # 代碼
        month = 2
        mavericks_schedule = GetAllTeamSchedules(team_code, month)

        if mavericks_schedule:
            messages = mavericks_schedule.get("獨行俠")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"獨行俠{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "獨行俠三月賽程":
        team_code = "mavericks"  # 代碼
        month = 3
        mavericks_schedule = GetAllTeamSchedules(team_code, month)

        if mavericks_schedule:
            messages = mavericks_schedule.get("獨行俠")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"獨行俠{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "獨行俠四月賽程":
        team_code = "mavericks"  # 代碼
        month = 4
        mavericks_schedule = GetAllTeamSchedules(team_code, month)

        if mavericks_schedule:
            messages = mavericks_schedule.get("獨行俠")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"獨行俠{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "金塊十月賽程":
        team_code = "nuggets"  # 代碼
        month = 10
        nuggets_schedule = GetAllTeamSchedules(team_code, month)

        if nuggets_schedule:
            messages = nuggets_schedule.get("掘金")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"掘金{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "金塊十一月賽程":
        team_code = "nuggets"  # 代碼
        month = 11
        nuggets_schedule = GetAllTeamSchedules(team_code, month)

        if nuggets_schedule:
            messages = nuggets_schedule.get("掘金")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"掘金{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "金塊十二月賽程":
        team_code = "nuggets"  # 代碼
        month = 12
        nuggets_schedule = GetAllTeamSchedules(team_code, month)

        if nuggets_schedule:
            messages = nuggets_schedule.get("掘金")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"掘金{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "金塊一月賽程":
        team_code = "nuggets"  # 代碼
        month = 1
        nuggets_schedule = GetAllTeamSchedules(team_code, month)

        if nuggets_schedule:
            messages = nuggets_schedule.get("掘金")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"掘金{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "金塊二月賽程":
        team_code = "nuggets"  # 代碼
        month = 2
        nuggets_schedule = GetAllTeamSchedules(team_code, month)

        if nuggets_schedule:
            messages = nuggets_schedule.get("掘金")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"掘金{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "金塊三月賽程":
        team_code = "nuggets"  # 代碼
        month = 3
        nuggets_schedule = GetAllTeamSchedules(team_code, month)

        if nuggets_schedule:
            messages = nuggets_schedule.get("掘金")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"掘金{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "金塊四月賽程":
        team_code = "nuggets"  # 代碼
        month = 4
        nuggets_schedule = GetAllTeamSchedules(team_code, month)

        if nuggets_schedule:
            messages = nuggets_schedule.get("掘金")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"掘金{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "勇士十月賽程":
        team_code = "warriors"  # 代碼
        month = 10
        warriors_schedule = GetAllTeamSchedules(team_code, month)

        if warriors_schedule:
            messages = warriors_schedule.get("勇士")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"勇士{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "勇士十一月賽程":
        team_code = "warriors"  # 代碼
        month = 11
        warriors_schedule = GetAllTeamSchedules(team_code, month)

        if warriors_schedule:
            messages = warriors_schedule.get("勇士")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"勇士{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "勇士十二月賽程":
        team_code = "warriors"  # 代碼
        month = 12
        warriors_schedule = GetAllTeamSchedules(team_code, month)

        if warriors_schedule:
            messages = warriors_schedule.get("勇士")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"勇士{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "勇士一月賽程":
        team_code = "warriors"  # 代碼
        month = 1
        warriors_schedule = GetAllTeamSchedules(team_code, month)

        if warriors_schedule:
            messages = warriors_schedule.get("勇士")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"勇士{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "勇士二月賽程":
        team_code = "warriors"  # 代碼
        month = 2
        warriors_schedule = GetAllTeamSchedules(team_code, month)

        if warriors_schedule:
            messages = warriors_schedule.get("勇士")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"勇士{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "勇士三月賽程":
        team_code = "warriors"  # 代碼
        month = 3
        warriors_schedule = GetAllTeamSchedules(team_code, month)

        if warriors_schedule:
            messages = warriors_schedule.get("勇士")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"勇士{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "勇士四月賽程":
        team_code = "warriors"  # 代碼
        month = 4
        warriors_schedule = GetAllTeamSchedules(team_code, month)

        if warriors_schedule:
            messages = warriors_schedule.get("勇士")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"勇士{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "火箭十月賽程":
        team_code = "rockets"  # 代碼
        month = 10
        rockets_schedule = GetAllTeamSchedules(team_code, month)

        if rockets_schedule:
            messages = rockets_schedule.get("火箭")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"火箭{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "火箭十一月賽程":
        team_code = "rockets"  # 代碼
        month = 11
        rockets_schedule = GetAllTeamSchedules(team_code, month)

        if rockets_schedule:
            messages = rockets_schedule.get("火箭")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"火箭{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "火箭十二月賽程":
        team_code = "rockets"  # 代碼
        month = 12
        rockets_schedule = GetAllTeamSchedules(team_code, month)

        if rockets_schedule:
            messages = rockets_schedule.get("火箭")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"火箭{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "火箭一月賽程":
        team_code = "rockets"  # 代碼
        month = 1
        rockets_schedule = GetAllTeamSchedules(team_code, month)

        if rockets_schedule:
            messages = rockets_schedule.get("火箭")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"火箭{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "火箭二月賽程":
        team_code = "rockets"  # 代碼
        month = 2
        rockets_schedule = GetAllTeamSchedules(team_code, month)

        if rockets_schedule:
            messages = rockets_schedule.get("火箭")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"火箭{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "火箭三月賽程":
        team_code = "rockets"  # 代碼
        month = 3
        rockets_schedule = GetAllTeamSchedules(team_code, month)

        if rockets_schedule:
            messages = rockets_schedule.get("火箭")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"火箭{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "火箭四月賽程":
        team_code = "rockets"  # 代碼
        month = 4
        rockets_schedule = GetAllTeamSchedules(team_code, month)

        if rockets_schedule:
            messages = rockets_schedule.get("火箭")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"火箭{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "灰狼十月賽程":
        team_code = "timberwolves"  # 代碼
        month = 10
        timberwolves_schedule = GetAllTeamSchedules(team_code, month)

        if timberwolves_schedule:
            messages = timberwolves_schedule.get("森林狼")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"森林狼{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "灰狼十一月賽程":
        team_code = "timberwolves"  # 代碼
        month = 11
        timberwolves_schedule = GetAllTeamSchedules(team_code, month)

        if timberwolves_schedule:
            messages = timberwolves_schedule.get("森林狼")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"森林狼{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "灰狼十二月賽程":
        team_code = "timberwolves"  # 代碼
        month = 12
        timberwolves_schedule = GetAllTeamSchedules(team_code, month)

        if timberwolves_schedule:
            messages = timberwolves_schedule.get("森林狼")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"森林狼{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "灰狼一月賽程":
        team_code = "timberwolves"  # 代碼
        month = 1
        timberwolves_schedule = GetAllTeamSchedules(team_code, month)

        if timberwolves_schedule:
            messages = timberwolves_schedule.get("森林狼")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"森林狼{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "灰狼二月賽程":
        team_code = "timberwolves"  # 代碼
        month = 2
        timberwolves_schedule = GetAllTeamSchedules(team_code, month)

        if timberwolves_schedule:
            messages = timberwolves_schedule.get("森林狼")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"森林狼{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "灰狼三月賽程":
        team_code = "timberwolves"  # 代碼
        month = 3
        timberwolves_schedule = GetAllTeamSchedules(team_code, month)

        if timberwolves_schedule:
            messages = timberwolves_schedule.get("森林狼")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"森林狼{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "灰狼四月賽程":
        team_code = "timberwolves"  # 代碼
        month = 4
        timberwolves_schedule = GetAllTeamSchedules(team_code, month)

        if timberwolves_schedule:
            messages = timberwolves_schedule.get("森林狼")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"森林狼{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "快艇十月賽程":
        team_code = "clippers"  # 代碼
        month = 10
        clippers_schedule = GetAllTeamSchedules(team_code, month)

        if clippers_schedule:
            messages = clippers_schedule.get("快船")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"快船{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "快艇十一月賽程":
        team_code = "clippers"  # 代碼
        month = 11
        clippers_schedule = GetAllTeamSchedules(team_code, month)

        if clippers_schedule:
            messages = clippers_schedule.get("快船")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"快船{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "快艇十二月賽程":
        team_code = "clippers"  # 代碼
        month = 12
        clippers_schedule = GetAllTeamSchedules(team_code, month)

        if clippers_schedule:
            messages = clippers_schedule.get("快船")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"快船{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "快艇一月賽程":
        team_code = "clippers"  # 代碼
        month = 1
        clippers_schedule = GetAllTeamSchedules(team_code, month)

        if clippers_schedule:
            messages = clippers_schedule.get("快船")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"快船{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "快艇二月賽程":
        team_code = "clippers"  # 代碼
        month = 2
        clippers_schedule = GetAllTeamSchedules(team_code, month)

        if clippers_schedule:
            messages = clippers_schedule.get("快船")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"快船{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "快艇三月賽程":
        team_code = "clippers"  # 代碼
        month = 3
        clippers_schedule = GetAllTeamSchedules(team_code, month)

        if clippers_schedule:
            messages = clippers_schedule.get("快船")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"快船{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "快艇四月賽程":
        team_code = "clippers"  # 代碼
        month = 4
        clippers_schedule = GetAllTeamSchedules(team_code, month)

        if clippers_schedule:
            messages = clippers_schedule.get("快船")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"快船{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "灰熊十月賽程":
        team_code = "grizzlies"  # 代碼
        month = 10
        grizzlies_schedule = GetAllTeamSchedules(team_code, month)

        if grizzlies_schedule:
            messages = grizzlies_schedule.get("灰熊")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"灰熊{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "灰熊十一月賽程":
        team_code = "grizzlies"  # 代碼
        month = 11
        grizzlies_schedule = GetAllTeamSchedules(team_code, month)

        if grizzlies_schedule:
            messages = grizzlies_schedule.get("灰熊")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"灰熊{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "灰熊十二月賽程":
        team_code = "grizzlies"  # 代碼
        month = 12
        grizzlies_schedule = GetAllTeamSchedules(team_code, month)

        if grizzlies_schedule:
            messages = grizzlies_schedule.get("灰熊")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"灰熊{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "灰熊一月賽程":
        team_code = "grizzlies"  # 代碼
        month = 1
        grizzlies_schedule = GetAllTeamSchedules(team_code, month)

        if grizzlies_schedule:
            messages = grizzlies_schedule.get("灰熊")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"灰熊{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "灰熊二月賽程":
        team_code = "grizzlies"  # 代碼
        month = 2
        grizzlies_schedule = GetAllTeamSchedules(team_code, month)

        if grizzlies_schedule:
            messages = grizzlies_schedule.get("灰熊")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"灰熊{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "灰熊三月賽程":
        team_code = "grizzlies"  # 代碼
        month = 3
        grizzlies_schedule = GetAllTeamSchedules(team_code, month)

        if grizzlies_schedule:
            messages = grizzlies_schedule.get("灰熊")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"灰熊{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "灰熊四月賽程":
        team_code = "grizzlies"  # 代碼
        month = 4
        grizzlies_schedule = GetAllTeamSchedules(team_code, month)

        if grizzlies_schedule:
            messages = grizzlies_schedule.get("灰熊")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"灰熊{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "雷霆十月賽程":
        team_code = "thunder"  # 代碼
        month = 10
        thunder_schedule = GetAllTeamSchedules(team_code, month)

        if thunder_schedule:
            messages = thunder_schedule.get("雷霆")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"雷霆{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "雷霆十一月賽程":
        team_code = "thunder"  # 代碼
        month = 11
        thunder_schedule = GetAllTeamSchedules(team_code, month)

        if thunder_schedule:
            messages = thunder_schedule.get("雷霆")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"雷霆{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "雷霆十二月賽程":
        team_code = "thunder"  # 代碼
        month = 12
        thunder_schedule = GetAllTeamSchedules(team_code, month)

        if thunder_schedule:
            messages = thunder_schedule.get("雷霆")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"雷霆{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "雷霆一月賽程":
        team_code = "thunder"  # 代碼
        month = 1
        thunder_schedule = GetAllTeamSchedules(team_code, month)

        if thunder_schedule:
            messages = thunder_schedule.get("雷霆")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"雷霆{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "雷霆二月賽程":
        team_code = "thunder"  # 代碼
        month = 2
        thunder_schedule = GetAllTeamSchedules(team_code, month)

        if thunder_schedule:
            messages = thunder_schedule.get("雷霆")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"雷霆{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "雷霆三月賽程":
        team_code = "thunder"  # 代碼
        month = 3
        thunder_schedule = GetAllTeamSchedules(team_code, month)

        if thunder_schedule:
            messages = thunder_schedule.get("雷霆")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"雷霆{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "雷霆四月賽程":
        team_code = "thunder"  # 代碼
        month = 4
        thunder_schedule = GetAllTeamSchedules(team_code, month)

        if thunder_schedule:
            messages = thunder_schedule.get("雷霆")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"雷霆{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "湖人十月賽程":
        team_code = "lakers"  # 代碼
        month = 10
        lakers_schedule = GetAllTeamSchedules(team_code, month)

        if lakers_schedule:
            messages = lakers_schedule.get("湖人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"湖人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "湖人十一月賽程":
        team_code = "lakers"  # 代碼
        month = 11
        lakers_schedule = GetAllTeamSchedules(team_code, month)

        if lakers_schedule:
            messages = lakers_schedule.get("湖人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"湖人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "湖人十二月賽程":
        team_code = "lakers"  # 代碼
        month = 12
        lakers_schedule = GetAllTeamSchedules(team_code, month)

        if lakers_schedule:
            messages = lakers_schedule.get("湖人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"湖人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "湖人一月賽程":
        team_code = "lakers"  # 代碼
        month = 1
        lakers_schedule = GetAllTeamSchedules(team_code, month)

        if lakers_schedule:
            messages = lakers_schedule.get("湖人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"湖人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "湖人二月賽程":
        team_code = "lakers"  # 代碼
        month = 2
        lakers_schedule = GetAllTeamSchedules(team_code, month)

        if lakers_schedule:
            messages = lakers_schedule.get("湖人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"湖人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "湖人三月賽程":
        team_code = "lakers"  # 代碼
        month = 3
        lakers_schedule = GetAllTeamSchedules(team_code, month)

        if lakers_schedule:
            messages = lakers_schedule.get("湖人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"湖人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "湖人四月賽程":
        team_code = "lakers"  # 代碼
        month = 4
        lakers_schedule = GetAllTeamSchedules(team_code, month)

        if lakers_schedule:
            messages = lakers_schedule.get("湖人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"湖人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "鵜鶘十月賽程":
        team_code = "pelicans"  # 代碼
        month = 10
        pelicans_schedule = GetAllTeamSchedules(team_code, month)

        if pelicans_schedule:
            messages = pelicans_schedule.get("鵜鶘")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"鵜鶘{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "鵜鶘十一月賽程":
        team_code = "pelicans"  # 代碼
        month = 11
        pelicans_schedule = GetAllTeamSchedules(team_code, month)

        if pelicans_schedule:
            messages = pelicans_schedule.get("鵜鶘")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"鵜鶘{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "鵜鶘十二月賽程":
        team_code = "pelicans"  # 代碼
        month = 12
        pelicans_schedule = GetAllTeamSchedules(team_code, month)

        if pelicans_schedule:
            messages = pelicans_schedule.get("鵜鶘")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"鵜鶘{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "鵜鶘一月賽程":
        team_code = "pelicans"  # 代碼
        month = 1
        pelicans_schedule = GetAllTeamSchedules(team_code, month)

        if pelicans_schedule:
            messages = pelicans_schedule.get("鵜鶘")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"鵜鶘{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "鵜鶘二月賽程":
        team_code = "pelicans"  # 代碼
        month = 2
        pelicans_schedule = GetAllTeamSchedules(team_code, month)

        if pelicans_schedule:
            messages = pelicans_schedule.get("鵜鶘")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"鵜鶘{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "鵜鶘三月賽程":
        team_code = "pelicans"  # 代碼
        month = 3
        pelicans_schedule = GetAllTeamSchedules(team_code, month)

        if pelicans_schedule:
            messages = pelicans_schedule.get("鵜鶘")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"鵜鶘{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "鵜鶘四月賽程":
        team_code = "pelicans"  # 代碼
        month = 4
        pelicans_schedule = GetAllTeamSchedules(team_code, month)

        if pelicans_schedule:
            messages = pelicans_schedule.get("鵜鶘")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"鵜鶘{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "拓荒者十月賽程":
        team_code = "blazers"  # 代碼
        month = 10
        blazers_schedule = GetAllTeamSchedules(team_code, month)

        if blazers_schedule:
            messages = blazers_schedule.get("開拓者")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"開拓者{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "拓荒者十一月賽程":
        team_code = "blazers"  # 代碼
        month = 11
        blazers_schedule = GetAllTeamSchedules(team_code, month)

        if blazers_schedule:
            messages = blazers_schedule.get("開拓者")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"開拓者{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "拓荒者十二月賽程":
        team_code = "blazers"  # 代碼
        month = 12
        blazers_schedule = GetAllTeamSchedules(team_code, month)

        if blazers_schedule:
            messages = blazers_schedule.get("開拓者")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"開拓者{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "拓荒者一月賽程":
        team_code = "blazers"  # 代碼
        month = 1
        blazers_schedule = GetAllTeamSchedules(team_code, month)

        if blazers_schedule:
            messages = blazers_schedule.get("開拓者")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"開拓者{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "拓荒者二月賽程":
        team_code = "blazers"  # 代碼
        month = 2
        blazers_schedule = GetAllTeamSchedules(team_code, month)

        if blazers_schedule:
            messages = blazers_schedule.get("開拓者")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"開拓者{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "拓荒者三月賽程":
        team_code = "blazers"  # 代碼
        month = 3
        blazers_schedule = GetAllTeamSchedules(team_code, month)

        if blazers_schedule:
            messages = blazers_schedule.get("開拓者")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"開拓者{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "拓荒者四月賽程":
        team_code = "blazers"  # 代碼
        month = 4
        blazers_schedule = GetAllTeamSchedules(team_code, month)

        if blazers_schedule:
            messages = blazers_schedule.get("開拓者")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"開拓者{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "太陽十月賽程":
        team_code = "suns"  # 代碼
        month = 10
        suns_schedule = GetAllTeamSchedules(team_code, month)

        if suns_schedule:
            messages = suns_schedule.get("太陽")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"太陽{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "太陽十一月賽程":
        team_code = "suns"  # 代碼
        month = 11
        suns_schedule = GetAllTeamSchedules(team_code, month)

        if suns_schedule:
            messages = suns_schedule.get("太陽")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"太陽{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "太陽十二月賽程":
        team_code = "suns"  # 代碼
        month = 12
        suns_schedule = GetAllTeamSchedules(team_code, month)

        if suns_schedule:
            messages = suns_schedule.get("太陽")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"太陽{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "太陽一月賽程":
        team_code = "suns"  # 代碼
        month = 1
        suns_schedule = GetAllTeamSchedules(team_code, month)

        if suns_schedule:
            messages = suns_schedule.get("太陽")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"太陽{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "太陽二月賽程":
        team_code = "suns"  # 代碼
        month = 2
        suns_schedule = GetAllTeamSchedules(team_code, month)

        if suns_schedule:
            messages = suns_schedule.get("太陽")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"太陽{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "太陽三月賽程":
        team_code = "suns"  # 代碼
        month = 3
        suns_schedule = GetAllTeamSchedules(team_code, month)

        if suns_schedule:
            messages = suns_schedule.get("太陽")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"太陽{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "太陽四月賽程":
        team_code = "suns"  # 代碼
        month = 4
        suns_schedule = GetAllTeamSchedules(team_code, month)

        if suns_schedule:
            messages = suns_schedule.get("太陽")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"太陽{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "馬刺十月賽程":
        team_code = "spurs"  # 代碼
        month = 10
        spurs_schedule = GetAllTeamSchedules(team_code, month)

        if spurs_schedule:
            messages = spurs_schedule.get("馬刺")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"馬刺{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "馬刺十一月賽程":
        team_code = "spurs"  # 代碼
        month = 11
        spurs_schedule = GetAllTeamSchedules(team_code, month)

        if spurs_schedule:
            messages = spurs_schedule.get("馬刺")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"馬刺{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "馬刺十二月賽程":
        team_code = "spurs"  # 代碼
        month = 12
        spurs_schedule = GetAllTeamSchedules(team_code, month)

        if spurs_schedule:
            messages = spurs_schedule.get("馬刺")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"馬刺{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "馬刺一月賽程":
        team_code = "spurs"  # 代碼
        month = 1
        spurs_schedule = GetAllTeamSchedules(team_code, month)

        if spurs_schedule:
            messages = spurs_schedule.get("馬刺")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"馬刺{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "馬刺二月賽程":
        team_code = "spurs"  # 代碼
        month = 2
        spurs_schedule = GetAllTeamSchedules(team_code, month)

        if spurs_schedule:
            messages = spurs_schedule.get("馬刺")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"馬刺{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "馬刺三月賽程":
        team_code = "spurs"  # 代碼
        month = 3
        spurs_schedule = GetAllTeamSchedules(team_code, month)

        if spurs_schedule:
            messages = spurs_schedule.get("馬刺")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"馬刺{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "馬刺四月賽程":
        team_code = "spurs"  # 代碼
        month = 4
        spurs_schedule = GetAllTeamSchedules(team_code, month)

        if spurs_schedule:
            messages = spurs_schedule.get("馬刺")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"馬刺{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "爵士十月賽程":
        team_code = "jazz"  # 代碼
        month = 10
        jazz_schedule = GetAllTeamSchedules(team_code, month)

        if jazz_schedule:
            messages = jazz_schedule.get("爵士")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"爵士{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "爵士十一月賽程":
        team_code = "jazz"  # 代碼
        month = 11
        jazz_schedule = GetAllTeamSchedules(team_code, month)

        if jazz_schedule:
            messages = jazz_schedule.get("爵士")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"爵士{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "爵士十二月賽程":
        team_code = "jazz"  # 代碼
        month = 12
        jazz_schedule = GetAllTeamSchedules(team_code, month)

        if jazz_schedule:
            messages = jazz_schedule.get("爵士")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"爵士{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "爵士一月賽程":
        team_code = "jazz"  # 代碼
        month = 1
        jazz_schedule = GetAllTeamSchedules(team_code, month)

        if jazz_schedule:
            messages = jazz_schedule.get("爵士")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"爵士{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "爵士二月賽程":
        team_code = "jazz"  # 代碼
        month = 2
        jazz_schedule = GetAllTeamSchedules(team_code, month)

        if jazz_schedule:
            messages = jazz_schedule.get("爵士")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"爵士{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "爵士三月賽程":
        team_code = "jazz"  # 代碼
        month = 3
        jazz_schedule = GetAllTeamSchedules(team_code, month)

        if jazz_schedule:
            messages = jazz_schedule.get("爵士")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"爵士{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "爵士四月賽程":
        team_code = "jazz"  # 代碼
        month = 4
        jazz_schedule = GetAllTeamSchedules(team_code, month)

        if jazz_schedule:
            messages = jazz_schedule.get("爵士")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"爵士{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "國王十月賽程":
        team_code = "kings"  # 代碼
        month = 10
        kings_schedule = GetAllTeamSchedules(team_code, month)

        if kings_schedule:
            messages = kings_schedule.get("國王")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"國王{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "國王十一月賽程":
        team_code = "kings"  # 代碼
        month = 11
        kings_schedule = GetAllTeamSchedules(team_code, month)

        if kings_schedule:
            messages = kings_schedule.get("國王")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"國王{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "國王十二月賽程":
        team_code = "kings"  # 代碼
        month = 12
        kings_schedule = GetAllTeamSchedules(team_code, month)

        if kings_schedule:
            messages = kings_schedule.get("國王")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"國王{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "國王一月賽程":
        team_code = "kings"  # 代碼
        month = 1
        kings_schedule = GetAllTeamSchedules(team_code, month)

        if kings_schedule:
            messages = kings_schedule.get("國王")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"國王{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "國王二月賽程":
        team_code = "kings"  # 代碼
        month = 2
        kings_schedule = GetAllTeamSchedules(team_code, month)

        if kings_schedule:
            messages = kings_schedule.get("國王")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"國王{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "國王三月賽程":
        team_code = "kings"  # 代碼
        month = 3
        kings_schedule = GetAllTeamSchedules(team_code, month)

        if kings_schedule:
            messages = kings_schedule.get("國王")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"國王{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "國王四月賽程":
        team_code = "kings"  # 代碼
        month = 4
        kings_schedule = GetAllTeamSchedules(team_code, month)

        if kings_schedule:
            messages = kings_schedule.get("國王")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"國王{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "76人十月賽程":
        team_code = "76ers"  # 代碼
        month = 10
        phi_schedule = GetAllTeamSchedules(team_code, month)

        if phi_schedule:
            messages = phi_schedule.get("76人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"76人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "76人十一月賽程":
        team_code = "76ers"  # 代碼
        month = 11
        phi_schedule = GetAllTeamSchedules(team_code, month)

        if phi_schedule:
            messages = phi_schedule.get("76人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"76人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "76人十二月賽程":
        team_code = "76ers"  # 代碼
        month = 12
        phi_schedule = GetAllTeamSchedules(team_code, month)

        if phi_schedule:
            messages = phi_schedule.get("76人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"76人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "76人一月賽程":
        team_code = "76ers"  # 代碼
        month = 1
        phi_schedule = GetAllTeamSchedules(team_code, month)

        if phi_schedule:
            messages = phi_schedule.get("76人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"76人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "76人二月賽程":
        team_code = "76ers"  # 代碼
        month = 2
        phi_schedule = GetAllTeamSchedules(team_code, month)

        if phi_schedule:
            messages = phi_schedule.get("76人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"76人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "76人三月賽程":
        team_code = "76ers"  # 代碼
        month = 3
        phi_schedule = GetAllTeamSchedules(team_code, month)

        if phi_schedule:
            messages = phi_schedule.get("76人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"76人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "76人四月賽程":
        team_code = "76ers"  # 代碼
        month = 4
        phi_schedule = GetAllTeamSchedules(team_code, month)

        if phi_schedule:
            messages = phi_schedule.get("76人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"76人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    
  
    if text == "七六人十月賽程":
        team_code = "76ers"  # 代碼
        month = 10
        phi_schedule = GetAllTeamSchedules(team_code, month)

        if phi_schedule:
            messages = phi_schedule.get("76人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"76人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "七六人十一月賽程":
        team_code = "76ers"  # 代碼
        month = 11
        phi_schedule = GetAllTeamSchedules(team_code, month)

        if phi_schedule:
            messages = phi_schedule.get("76人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"76人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "七六人十二月賽程":
        team_code = "76ers"  # 代碼
        month = 12
        phi_schedule = GetAllTeamSchedules(team_code, month)

        if phi_schedule:
            messages = phi_schedule.get("76人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"76人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "七六人一月賽程":
        team_code = "76ers"  # 代碼
        month = 1
        phi_schedule = GetAllTeamSchedules(team_code, month)

        if phi_schedule:
            messages = phi_schedule.get("76人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"76人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "七六人二月賽程":
        team_code = "76ers"  # 代碼
        month = 2
        phi_schedule = GetAllTeamSchedules(team_code, month)

        if phi_schedule:
            messages = phi_schedule.get("76人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"76人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "七六人三月賽程":
        team_code = "76ers"  # 代碼
        month = 3
        phi_schedule = GetAllTeamSchedules(team_code, month)

        if phi_schedule:
            messages = phi_schedule.get("76人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"76人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "76人四月賽程":
        team_code = "76ers"  # 代碼
        month = 4
        phi_schedule = GetAllTeamSchedules(team_code, month)

        if phi_schedule:
            messages = phi_schedule.get("76人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"76人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0   
    
    if text == "七六人10月賽程":
        team_code = "76ers"  # 代碼
        month = 10
        phi_schedule = GetAllTeamSchedules(team_code, month)

        if phi_schedule:
            messages = phi_schedule.get("76人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"76人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "七六人11月賽程":
        team_code = "76ers"  # 代碼
        month = 11
        phi_schedule = GetAllTeamSchedules(team_code, month)

        if phi_schedule:
            messages = phi_schedule.get("76人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"76人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "七六人12月賽程":
        team_code = "76ers"  # 代碼
        month = 12
        phi_schedule = GetAllTeamSchedules(team_code, month)

        if phi_schedule:
            messages = phi_schedule.get("76人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"76人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "七六人1月賽程":
        team_code = "76ers"  # 代碼
        month = 1
        phi_schedule = GetAllTeamSchedules(team_code, month)

        if phi_schedule:
            messages = phi_schedule.get("76人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"76人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "七六人2月賽程":
        team_code = "76ers"  # 代碼
        month = 2
        phi_schedule = GetAllTeamSchedules(team_code, month)

        if phi_schedule:
            messages = phi_schedule.get("76人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"76人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0

    if text == "七六人3月賽程":
        team_code = "76ers"  # 代碼
        month = 3
        phi_schedule = GetAllTeamSchedules(team_code, month)

        if phi_schedule:
            messages = phi_schedule.get("76人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"76人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "七六人4月賽程":
        team_code = "76ers"  # 代碼
        month = 4
        phi_schedule = GetAllTeamSchedules(team_code, month)

        if phi_schedule:
            messages = phi_schedule.get("76人")
            if messages and len(messages) > 0:
                # 構建回覆消息
                reply_message = TextSendMessage(
                    f"76人{month}月賽程：\n" + "\n".join(messages)
                )
            else:
                reply_message = TextSendMessage(f"暫無{month}月賽程信息。")
            line_bot_api.reply_message(event.reply_token, reply_message)
        return 0
    
    if text == "七六人今年戰績":
        content_arr = []
        team_name = "七六人"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你七六人球隊今年戰績"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "76人今年戰績":
        content_arr = []
        team_name = "76人"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你76人球隊今年戰績"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "公牛今年戰績排名":
        content_arr = []
        team_name = "公牛"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你公牛球隊今年戰績"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "公鹿今年戰績":
        content_arr = []
        team_name = "公鹿"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你公鹿球隊今年戰績"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "太陽今年戰績":
        content_arr = []
        team_name = "太陽"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你太陽球隊今年戰績"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "火箭今年戰績":
        content_arr = []
        team_name = "火箭"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你火箭球隊今年戰績"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "尼克今年戰績":
        content_arr = []
        team_name = "尼克"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你尼克球隊今年戰績"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "灰狼今年戰績":
        content_arr = []
        team_name = "灰狼"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你灰狼球隊今年戰績"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "灰熊今年戰績":
        content_arr = []
        team_name = "灰熊"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你灰熊球隊今年戰績"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "老鷹今年戰績":
        content_arr = []
        team_name = "老鷹"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你老鷹球隊今年戰績"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "巫師今年戰績":
        content_arr = []
        team_name = "巫師"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你巫師球隊今年戰績"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "快艇今年戰績":
        content_arr = []
        team_name = "快艇"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你快艇球隊今年戰績"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "拓荒者今年戰績":
        content_arr = []
        team_name = "拓荒者"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你拓荒者球隊今年戰績"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "金塊今年戰績":
        content_arr = []
        team_name = "金塊"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你金塊球隊今年戰績"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "勇士今年戰績":
        content_arr = []
        team_name = "勇士"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你勇士球隊今年戰績"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "活塞今年戰績":
        content_arr = []
        team_name = "活塞"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你活塞球隊今年戰績"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "馬刺今年戰績":
        content_arr = []
        team_name = "馬刺"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你馬刺球隊今年戰績"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "國王今年戰績":
        content_arr = []
        team_name = "國王"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你國王球隊今年戰績"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "湖人今年戰績":
        content_arr = []
        team_name = "湖人"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你湖人球隊今年戰績"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "黃蜂今年戰績":
        content_arr = []
        team_name = "黃蜂"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你黃蜂球隊今年戰績"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "塞爾提克今年戰績":
        content_arr = []
        team_name = "塞爾提克"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你塞爾提克球隊今年戰績"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "溜馬今年戰績":
        content_arr = []
        team_name = "溜馬"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你溜馬球隊今年戰績"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "雷霆今年戰績":
        content_arr = []
        team_name = "雷霆"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你雷霆球隊今年戰績"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "暴龍今年戰績":
        content_arr = []
        team_name = "暴龍"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你暴龍球隊今年戰績"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "熱火今年戰績":
        content_arr = []
        team_name = "熱火"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你熱火球隊今年戰績"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "獨行俠今年戰績":
        content_arr = []
        team_name = "獨行俠"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你獨行俠球隊今年戰績"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "爵士今年戰績":
        content_arr = []
        team_name = "爵士"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你爵士球隊今年戰績"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "騎士今年戰績":
        content_arr = []
        team_name = "騎士"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你騎士球隊今年戰績"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "鵜鶘今年戰績":
        content_arr = []
        team_name = "鵜鶘"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你鵜鶘球隊今年戰績"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "籃網今年戰績":
        content_arr = []
        team_name = "籃網"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你籃網球隊今年戰績"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0

    if text == "魔術今年戰績":
        content_arr = []
        team_name = "魔術"
        team_stats = GetTeamStanding(team_name)
        content_arr.append(TextSendMessage(team_stats))
        content_arr.append(TextSendMessage("以上提供給你魔術球隊今年戰績"))
        line_bot_api.reply_message(event.reply_token, content_arr)
        return 0
    
    if text == "巫師賽程":
            content_arr = []
            content_arr.append(TextSendMessage("請輸入巫師\n加上月份賽程"))
            content_arr.append(TextSendMessage("例如:巫師十月賽程"))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "黃蜂賽程":
            content_arr = []
            content_arr.append(TextSendMessage("請輸入黃蜂伍\n加上月份賽程"))
            content_arr.append(TextSendMessage("例如:黃蜂十月賽程"))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "老鷹賽程":
            content_arr = []
            content_arr.append(TextSendMessage("請輸入老鷹\n加上月份賽程"))
            content_arr.append(TextSendMessage("例如:老鷹十月賽程"))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "熱火賽程":
            content_arr = []
            content_arr.append(TextSendMessage("請輸入熱火\n加上月份賽程"))
            content_arr.append(TextSendMessage("例如:熱火十月賽程"))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "魔術賽程":
            content_arr = []
            content_arr.append(TextSendMessage("請輸入魔術\n加上月份賽程"))
            content_arr.append(TextSendMessage("例如:魔術十月賽程"))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "尼克賽程":
            content_arr = []
            content_arr.append(TextSendMessage("請輸入尼克\n加上月份賽程"))
            content_arr.append(TextSendMessage("例如:尼克十月賽程"))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "76人賽程":
            content_arr = []
            content_arr.append(TextSendMessage("請輸入76人\n加上月份賽程"))
            content_arr.append(TextSendMessage("例如:76人十月賽程"))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "七六人賽程":
            content_arr = []
            content_arr.append(TextSendMessage("請輸入七六人\n加上月份賽程"))
            content_arr.append(TextSendMessage("例如:七六人十月賽程"))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "籃網賽程":
            content_arr = []
            content_arr.append(TextSendMessage("請輸入籃網\n加上月份賽程"))
            content_arr.append(TextSendMessage("例如:籃網十月賽程"))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "塞爾提克賽程":
            content_arr = []
            content_arr.append(TextSendMessage("請輸入塞爾提克\n加上月份賽程"))
            content_arr.append(TextSendMessage("例如:塞爾提克十月賽程"))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "暴龍賽程":
            content_arr = []
            content_arr.append(TextSendMessage("請輸入暴龍\n加上月份賽程"))
            content_arr.append(TextSendMessage("例如:暴龍十月賽程"))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "公牛賽程":
            content_arr = []
            content_arr.append(TextSendMessage("請輸入公牛\n加上月份賽程"))
            content_arr.append(TextSendMessage("例如:公牛十月賽程"))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "騎士賽程":
            content_arr = []
            content_arr.append(TextSendMessage("請輸入騎士\n加上月份賽程"))
            content_arr.append(TextSendMessage("例如:騎士十月賽程"))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "溜馬賽程":
            content_arr = []
            content_arr.append(TextSendMessage("請輸入溜馬\n加上月份賽程"))
            content_arr.append(TextSendMessage("例如:溜馬十月賽程"))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "活塞賽程":
            content_arr = []
            content_arr.append(TextSendMessage("請輸入活塞\n加上月份賽程"))
            content_arr.append(TextSendMessage("例如:活塞十月賽程"))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "公鹿賽程":
            content_arr = []
            content_arr.append(TextSendMessage("請輸入公鹿\n加上月份賽程"))
            content_arr.append(TextSendMessage("例如:公鹿十月賽程"))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "灰狼賽程":
            content_arr = []
            content_arr.append(TextSendMessage("請輸入灰狼\n加上月份賽程"))
            content_arr.append(TextSendMessage("例如:灰狼十月賽程"))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "爵士賽程":
            content_arr = []
            content_arr.append(TextSendMessage("請輸入爵士\n加上月份賽程"))
            content_arr.append(TextSendMessage("例如:爵士十月賽程"))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "雷霆賽程":
            content_arr = []
            content_arr.append(TextSendMessage("請輸入雷霆\n加上月份賽程"))
            content_arr.append(TextSendMessage("例如:雷霆十月賽程"))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "拓荒者賽程":
            content_arr = []
            content_arr.append(TextSendMessage("請輸入拓荒者\n加上月份賽程"))
            content_arr.append(TextSendMessage("例如:拓荒者十月賽程"))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "金塊賽程":
            content_arr = []
            content_arr.append(TextSendMessage("請輸入金塊\n加上月份賽程"))
            content_arr.append(TextSendMessage("例如:金塊十月賽程"))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "灰熊賽程":
            content_arr = []
            content_arr.append(TextSendMessage("請輸入灰熊\n加上月份賽程"))
            content_arr.append(TextSendMessage("例如:灰熊十月賽程"))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "火箭賽程":
            content_arr = []
            content_arr.append(TextSendMessage("請輸入火箭\n加上月份賽程"))
            content_arr.append(TextSendMessage("例如:火箭十月賽程"))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "鵜鶘賽程":
            content_arr = []
            content_arr.append(TextSendMessage("請輸入鵜鶘\n加上月份賽程"))
            content_arr.append(TextSendMessage("例如:鵜鶘十月賽程"))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "馬刺賽程":
            content_arr = []
            content_arr.append(TextSendMessage("請輸入馬刺\n加上月份賽程"))
            content_arr.append(TextSendMessage("例如:馬刺十月賽程"))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "獨行俠賽程":
            content_arr = []
            content_arr.append(TextSendMessage("請輸入獨行俠\n加上月份賽程"))
            content_arr.append(TextSendMessage("例如:獨行俠十月賽程"))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "勇士賽程":
            content_arr = []
            content_arr.append(TextSendMessage("請輸入勇士\n加上月份賽程"))
            content_arr.append(TextSendMessage("例如:勇士十月賽程"))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "湖人賽程":
            content_arr = []
            content_arr.append(TextSendMessage("請輸入湖人\n加上月份賽程"))
            content_arr.append(TextSendMessage("例如:湖人十月賽程"))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "快艇賽程":
            content_arr = []
            content_arr.append(TextSendMessage("請輸入快艇\n加上月份賽程"))
            content_arr.append(TextSendMessage("例如:快艇十月賽程"))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "太陽賽程":
            content_arr = []
            content_arr.append(TextSendMessage("請輸入太陽\n加上月份賽程"))
            content_arr.append(TextSendMessage("例如:太陽十月賽程"))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
    if text == "國王賽程":
            content_arr = []
            content_arr.append(TextSendMessage("請輸入國王\n加上月份賽程"))
            content_arr.append(TextSendMessage("例如:國王十月賽程"))
            line_bot_api.reply_message(event.reply_token, content_arr)
            return 0
# 主程式
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 80))
    app.run(host="0.0.0.0", port=port)
