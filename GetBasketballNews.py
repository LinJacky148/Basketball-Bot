# 最新新聞
from bs4 import BeautifulSoup
import requests
from linebot.models import TextSendMessage

def UdnNews():
    url = "https://tw-nba.udn.com/nba/news/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    news_list = []
    for tag in soup.find_all("dt"):
        content = tag.a
        title_element = content.find("h3")
        if title_element:
            title = title_element.text.strip()
            thumbnail = content.find("img")["data-src"]
            article_link = content["href"]
            news_message = f"標題: {title}\n縮圖連結: {thumbnail}\n文章連結: {article_link}"
            news_list.append(TextSendMessage(text=news_message))
        

    # 如果找到新聞，就返回新聞訊息清單
    if news_list:
        return news_list
    else:
        # 如果找不到新聞，就返回一條訊息
        return [TextSendMessage(text="抱歉，找不到最近的新聞。")]
