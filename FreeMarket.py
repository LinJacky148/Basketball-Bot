# 自由市場消息
import pandas as pd
import requests
from bs4 import BeautifulSoup


def FreeMarket():
    url = "https://www.ptt.cc/bbs/NBA/search?q=author%3Alaigei"

    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    # 尋找包含 "自由市場" 的新聞標題和內容
    FreeMarket_related_news = []
    found_related_news = False  # 用來標記是否找到相關新聞

    for tag in soup.find_all("div", class_="r-ent"):
        title_element = tag.find("div", class_="title")
        if title_element and title_element.a:
            title = title_element.text.strip()
            article_link = "https://www.ptt.cc" + title_element.a["href"]
            if "自由市場" in title:
                # 將新聞標題和連結作為文字字串返回
                FreeMarket_related_news.append(f"標題: {title}\n文章連結: {article_link}")
                found_related_news = True

    # 如果找不到相關新聞，返回提示訊息
    if not found_related_news:
        return "抱歉，找不到關於 自由市場 最近的新聞。"

    # 將所有新聞字串結合為一個字串，以換行分隔
    return "\n".join(FreeMarket_related_news)
