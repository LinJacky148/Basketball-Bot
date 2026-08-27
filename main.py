from flask import Flask, request, abort
import json, datetime
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
from linebot.v3.messaging import MessagingApi
from GetDateScore import GetDateScore
from GetTeam import GetTeam, GetTeam2, GetTeam3
from GetAllSchedule import GetAllSchedule
from GetDateSchedule import GetDateSchedule
from GetPlayers import GetPlayers
from GetPlayer import GetPlayer
from GetTeamLeaders import GetTeamLeaders

app = Flask(__name__)
# LINE BOT info
line_bot_api = LineBotApi("1G0oDurewArggbrHdnRLWt2q3u7B5DITpg7lJzKJh+9KfarNgLlPLTQ5X6hETgAMUNg4ZXBf4D0rI5QfeTr7pJBb913t1c8DrZNEyJ4ZGvg6NIO0oyUqdu3S/QcFle84tZZ+bI+2RNtV0r79E9xagAdB04t89/1O/w1cDnyilFU=", timeout=10)
handler = WebhookHandler("2c33ca2d6a5b19290e79a3e000262f19")
messaging_api = MessagingApi(line_bot_api)

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

def reply_flex_message(reply_token, alt_text, contents):
    try:
        messaging_api.reply_message(reply_token, FlexSendMessage(alt_text=alt_text, contents=contents))
    except Exception as e:
        app.logger.error(f"Error sending reply: {e}")

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    reply_token = event.reply_token
    message = event.message.text

    if message == '過去戰績':
        Buttom = json.load(open('json/Score/Buttom.json','r',encoding='utf-8'))
        reply_flex_message(reply_token, '請選擇時間', Buttom)
    elif message == '本日戰績':
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        Card = GetDateScore(today)
        reply_flex_message(reply_token, '查詢結果出爐~', Card)
    elif(message == '球隊賽程'):
            line_bot_api.reply_message(reply_token, FlexSendMessage('請選擇球隊', GetTeam()))
    elif(message == '球員數據'):
            line_bot_api.reply_message(reply_token, FlexSendMessage('請選擇球隊', GetTeam2()))
    elif(message == '球隊數據排行'):
            line_bot_api.reply_message(reply_token, FlexSendMessage('請選擇球隊', GetTeam3()))

@handler.add(PostbackEvent)
def handle_postback(event):
    reply_token = event.reply_token
    data = event.postback.data


    if data == 'SelectTime':
        date = event.postback.params['date']
        Card = GetDateScore(date)
        reply_flex_message(reply_token, '查詢結果出爐~', Card)
    elif data.startswith('Get'):
        date = data[3:]
        Card = GetDateScore(date)
        line_bot_api.reply_message(reply_token, FlexSendMessage('查詢結果出爐~', Card))
    elif(data.startswith('SelectScheduleFrom')):
        Team = data.split()[1]
        Card = GetAllSchedule(Team)
        line_bot_api.reply_message(reply_token, FlexSendMessage('查詢結果出爐~', Card))
    elif(data.startswith('Schedule')):
        data = data.split()
        Team = data[1]
        Date = data[2]
        Card = GetDateSchedule(Team, Date)
        line_bot_api.reply_message(reply_token, FlexSendMessage('查詢結果出爐~', Card))
    elif(data.startswith('SelectPlayerFrom')):
        Team = data.split()[1]
        Card = GetPlayers(Team)
        line_bot_api.reply_message(reply_token, FlexSendMessage('請選擇球員~', Card))
    elif(data.startswith('SelectPlayerName')):
        PlayerName = data.split()[1]
        Card = GetPlayer(PlayerName)
        line_bot_api.reply_message(reply_token, FlexSendMessage('查詢結果出爐~', Card))
    elif(data.startswith('SelectLeaderFrom')):
        Team = data.split()[1]
        Card = GetTeamLeaders(Team)
        line_bot_api.reply_message(reply_token, FlexSendMessage('查詢結果出爐~', Card))
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port)
