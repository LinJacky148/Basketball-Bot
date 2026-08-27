# 各球隊新聞
import requests
from bs4 import BeautifulSoup
from linebot.models import TextSendMessage


def getaNews():
    # 定義要爬取的湖人新聞網頁URL
    url = "https://tw-nba.udn.com/search/tag/76人"

    # 發送HTTP請求並獲取響應
    response = requests.get(url)

    # 使用BeautifulSoup解析HTML響應
    soup = BeautifulSoup(response.content, "html.parser")

    # 找到所有包含勇士新聞的標題和連結

    a_news = []

    for tag in soup.find_all("li"):
        content = tag.a
        title_element = content.find("h2")
        if title_element:
            title = title_element.text
            thumbnail = content.find("img")["data-src"]
            article_link = content["href"]
            news_message = f"標題: {title}\n縮圖連結: {thumbnail}\n文章連結: {article_link}"
            a_news.append(TextSendMessage(text=news_message))

    # 如果找到新聞，就返回新聞訊息清單
    if a_news:
        return a_news
    else:
        # 如果找不到新聞，就返回一條訊息
        return [TextSendMessage(text="抱歉，找不到76人最近的新聞。")]


def getbNews():
    # 定義要爬取的湖人新聞網頁URL
    url = "https://tw-nba.udn.com/search/tag/公牛"

    # 發送HTTP請求並獲取響應
    response = requests.get(url)

    # 使用BeautifulSoup解析HTML響應
    soup = BeautifulSoup(response.content, "html.parser")

    # 找到所有包含湖人新聞的標題和連結
    b_news = []

    for tag in soup.find_all("li"):
        content = tag.a
        title_element = content.find("h2")
        if title_element:
            title = title_element.text
            thumbnail = content.find("img")["data-src"]
            article_link = content["href"]
            news_message = f"標題: {title}\n縮圖連結: {thumbnail}\n文章連結: {article_link}"
            b_news.append(TextSendMessage(text=news_message))

    # 如果找到新聞，就返回新聞訊息清單
    if b_news:
        return b_news
    else:
        # 如果找不到新聞，就返回一條訊息
        return [TextSendMessage(text="抱歉，找不到公牛最近的新聞。")]


def getcNews():
    # 定義要爬取的湖人新聞網頁URL
    url = "https://tw-nba.udn.com/search/tag/公鹿"

    # 發送HTTP請求並獲取響應
    response = requests.get(url)

    # 使用BeautifulSoup解析HTML響應
    soup = BeautifulSoup(response.content, "html.parser")

    # 找到所有包含太陽新聞的標題和連結
    c_news = []

    for tag in soup.find_all("li"):
        content = tag.a
        title_element = content.find("h2")
        if title_element:
            title = title_element.text
            thumbnail = content.find("img")["data-src"]
            article_link = content["href"]
            news_message = f"標題: {title}\n縮圖連結: {thumbnail}\n文章連結: {article_link}"
            c_news.append(TextSendMessage(text=news_message))

    # 如果找到新聞，就返回新聞訊息清單
    if c_news:
        return c_news
    else:
        # 如果找不到新聞，就返回一條訊息
        return [TextSendMessage(text="抱歉，找不到公鹿最近的新聞。")]


def getdNews():
    # 定義要爬取的湖人新聞網頁URL
    url = "https://tw-nba.udn.com/search/tag/太陽"

    # 發送HTTP請求並獲取響應
    response = requests.get(url)

    # 使用BeautifulSoup解析HTML響應
    soup = BeautifulSoup(response.content, "html.parser")

    # 找到所有包含太陽新聞的標題和連結
    d_news = []

    for tag in soup.find_all("li"):
        content = tag.a
        title_element = content.find("h2")
        if title_element:
            title = title_element.text
            thumbnail = content.find("img")["data-src"]
            article_link = content["href"]
            news_message = f"標題: {title}\n縮圖連結: {thumbnail}\n文章連結: {article_link}"
            d_news.append(TextSendMessage(text=news_message))

    # 如果找到新聞，就返回新聞訊息清單
    if d_news:
        return d_news
    else:
        # 如果找不到新聞，就返回一條訊息
        return [TextSendMessage(text="抱歉，找不到太陽最近的新聞。")]
    
def geteNews():
    # 定義要爬取的湖人新聞網頁URL
    url = "https://tw-nba.udn.com/search/tag/火箭"

    # 發送HTTP請求並獲取響應
    response = requests.get(url)

    # 使用BeautifulSoup解析HTML響應
    soup = BeautifulSoup(response.content, "html.parser")

    # 找到所有包含太陽新聞的標題和連結
    e_news = []

    for tag in soup.find_all("li"):
        content = tag.a
        title_element = content.find("h2")
        if title_element:
            title = title_element.text
            thumbnail = content.find("img")["data-src"]
            article_link = content["href"]
            news_message = f"標題: {title}\n縮圖連結: {thumbnail}\n文章連結: {article_link}"
            e_news.append(TextSendMessage(text=news_message))

    # 如果找到新聞，就返回新聞訊息清單
    if e_news:
        return e_news
    else:
        # 如果找不到新聞，就返回一條訊息
        return [TextSendMessage(text="抱歉，找不到火箭最近的新聞。")]
    
def getfNews():
    # 定義要爬取的湖人新聞網頁URL
    url = "https://tw-nba.udn.com/search/tag/尼克"

    # 發送HTTP請求並獲取響應
    response = requests.get(url)

    # 使用BeautifulSoup解析HTML響應
    soup = BeautifulSoup(response.content, "html.parser")

    # 找到所有包含太陽新聞的標題和連結
    f_news = []

    for tag in soup.find_all("li"):
        content = tag.a
        title_element = content.find("h2")
        if title_element:
            title = title_element.text
            thumbnail = content.find("img")["data-src"]
            article_link = content["href"]
            news_message = f"標題: {title}\n縮圖連結: {thumbnail}\n文章連結: {article_link}"
            f_news.append(TextSendMessage(text=news_message))

    # 如果找到新聞，就返回新聞訊息清單
    if f_news:
        return f_news
    else:
        # 如果找不到新聞，就返回一條訊息
        return [TextSendMessage(text="抱歉，找不到尼克最近的新聞。")]

def getgNews():
    # 定義要爬取的湖人新聞網頁URL
    url = "https://tw-nba.udn.com/search/tag/灰狼"

    # 發送HTTP請求並獲取響應
    response = requests.get(url)

    # 使用BeautifulSoup解析HTML響應
    soup = BeautifulSoup(response.content, "html.parser")

    # 找到所有包含太陽新聞的標題和連結
    g_news = []

    for tag in soup.find_all("li"):
        content = tag.a
        title_element = content.find("h2")
        if title_element:
            title = title_element.text
            thumbnail = content.find("img")["data-src"]
            article_link = content["href"]
            news_message = f"標題: {title}\n縮圖連結: {thumbnail}\n文章連結: {article_link}"
            g_news.append(TextSendMessage(text=news_message))

    # 如果找到新聞，就返回新聞訊息清單
    if g_news:
        return g_news
    else:
        # 如果找不到新聞，就返回一條訊息
        return [TextSendMessage(text="抱歉，找不到灰狼最近的新聞。")]

def gethNews():
    # 定義要爬取的湖人新聞網頁URL
    url = "https://tw-nba.udn.com/search/tag/灰熊"

    # 發送HTTP請求並獲取響應
    response = requests.get(url)

    # 使用BeautifulSoup解析HTML響應
    soup = BeautifulSoup(response.content, "html.parser")

    # 找到所有包含太陽新聞的標題和連結
    h_news = []

    for tag in soup.find_all("li"):
        content = tag.a
        title_element = content.find("h2")
        if title_element:
            title = title_element.text
            thumbnail = content.find("img")["data-src"]
            article_link = content["href"]
            news_message = f"標題: {title}\n縮圖連結: {thumbnail}\n文章連結: {article_link}"
            h_news.append(TextSendMessage(text=news_message))

    # 如果找到新聞，就返回新聞訊息清單
    if h_news:
        return h_news
    else:
        # 如果找不到新聞，就返回一條訊息
        return [TextSendMessage(text="抱歉，找不到灰熊最近的新聞。")]
    
def getiNews():
    # 定義要爬取的湖人新聞網頁URL
    url = "https://tw-nba.udn.com/search/tag/老鷹"

    # 發送HTTP請求並獲取響應
    response = requests.get(url)

    # 使用BeautifulSoup解析HTML響應
    soup = BeautifulSoup(response.content, "html.parser")

    # 找到所有包含太陽新聞的標題和連結
    i_news = []

    for tag in soup.find_all("li"):
        content = tag.a
        title_element = content.find("h2")
        if title_element:
            title = title_element.text
            thumbnail = content.find("img")["data-src"]
            article_link = content["href"]
            news_message = f"標題: {title}\n縮圖連結: {thumbnail}\n文章連結: {article_link}"
            i_news.append(TextSendMessage(text=news_message))

    # 如果找到新聞，就返回新聞訊息清單
    if i_news:
        return i_news
    else:
        # 如果找不到新聞，就返回一條訊息
        return [TextSendMessage(text="抱歉，找不到老鷹最近的新聞。")]
    
def getjNews():
    # 定義要爬取的湖人新聞網頁URL
    url = "https://tw-nba.udn.com/search/tag/巫師"

    # 發送HTTP請求並獲取響應
    response = requests.get(url)

    # 使用BeautifulSoup解析HTML響應
    soup = BeautifulSoup(response.content, "html.parser")

    # 找到所有包含太陽新聞的標題和連結
    j_news = []

    for tag in soup.find_all("li"):
        content = tag.a
        title_element = content.find("h2")
        if title_element:
            title = title_element.text
            thumbnail = content.find("img")["data-src"]
            article_link = content["href"]
            news_message = f"標題: {title}\n縮圖連結: {thumbnail}\n文章連結: {article_link}"
            j_news.append(TextSendMessage(text=news_message))

    # 如果找到新聞，就返回新聞訊息清單
    if j_news:
        return j_news
    else:
        # 如果找不到新聞，就返回一條訊息
        return [TextSendMessage(text="抱歉，找不到巫師最近的新聞。")]
    
def getkNews():
    # 定義要爬取的湖人新聞網頁URL
    url = "https://tw-nba.udn.com/search/tag/快艇"

    # 發送HTTP請求並獲取響應
    response = requests.get(url)

    # 使用BeautifulSoup解析HTML響應
    soup = BeautifulSoup(response.content, "html.parser")

    # 找到所有包含太陽新聞的標題和連結
    k_news = []

    for tag in soup.find_all("li"):
        content = tag.a
        title_element = content.find("h2")
        if title_element:
            title = title_element.text
            thumbnail = content.find("img")["data-src"]
            article_link = content["href"]
            news_message = f"標題: {title}\n縮圖連結: {thumbnail}\n文章連結: {article_link}"
            k_news.append(TextSendMessage(text=news_message))

    # 如果找到新聞，就返回新聞訊息清單
    if k_news:
        return k_news
    else:
        # 如果找不到新聞，就返回一條訊息
        return [TextSendMessage(text="抱歉，找不到快艇最近的新聞。")]
    
def getlNews():
    # 定義要爬取的湖人新聞網頁URL
    url = "https://tw-nba.udn.com/search/tag/拓荒者"

    # 發送HTTP請求並獲取響應
    response = requests.get(url)

    # 使用BeautifulSoup解析HTML響應
    soup = BeautifulSoup(response.content, "html.parser")

    # 找到所有包含太陽新聞的標題和連結
    l_news = []

    for tag in soup.find_all("li"):
        content = tag.a
        title_element = content.find("h2")
        if title_element:
            title = title_element.text
            thumbnail = content.find("img")["data-src"]
            article_link = content["href"]
            news_message = f"標題: {title}\n縮圖連結: {thumbnail}\n文章連結: {article_link}"
            l_news.append(TextSendMessage(text=news_message))

    # 如果找到新聞，就返回新聞訊息清單
    if l_news:
        return l_news
    else:
        # 如果找不到新聞，就返回一條訊息
        return [TextSendMessage(text="抱歉，找不到快艇最近的新聞。")]
    
def getmNews():
    # 定義要爬取的湖人新聞網頁URL
    url = "https://tw-nba.udn.com/search/tag/金塊"

    # 發送HTTP請求並獲取響應
    response = requests.get(url)

    # 使用BeautifulSoup解析HTML響應
    soup = BeautifulSoup(response.content, "html.parser")

    # 找到所有包含太陽新聞的標題和連結
    m_news = []

    for tag in soup.find_all("li"):
        content = tag.a
        title_element = content.find("h2")
        if title_element:
            title = title_element.text
            thumbnail = content.find("img")["data-src"]
            article_link = content["href"]
            news_message = f"標題: {title}\n縮圖連結: {thumbnail}\n文章連結: {article_link}"
            m_news.append(TextSendMessage(text=news_message))

    # 如果找到新聞，就返回新聞訊息清單
    if m_news:
        return m_news
    else:
        # 如果找不到新聞，就返回一條訊息
        return [TextSendMessage(text="抱歉，找不到金塊最近的新聞。")]
    
def getnNews():
    # 定義要爬取的湖人新聞網頁URL
    url = "https://tw-nba.udn.com/search/tag/勇士"

    # 發送HTTP請求並獲取響應
    response = requests.get(url)

    # 使用BeautifulSoup解析HTML響應
    soup = BeautifulSoup(response.content, "html.parser")

    # 找到所有包含太陽新聞的標題和連結
    n_news = []

    for tag in soup.find_all("li"):
        content = tag.a
        title_element = content.find("h2")
        if title_element:
            title = title_element.text
            thumbnail = content.find("img")["data-src"]
            article_link = content["href"]
            news_message = f"標題: {title}\n縮圖連結: {thumbnail}\n文章連結: {article_link}"
            n_news.append(TextSendMessage(text=news_message))

    # 如果找到新聞，就返回新聞訊息清單
    if n_news:
        return n_news
    else:
        # 如果找不到新聞，就返回一條訊息
        return [TextSendMessage(text="抱歉，找不到勇士最近的新聞。")]
    
def getoNews():
    # 定義要爬取的湖人新聞網頁URL
    url = "https://tw-nba.udn.com/search/tag/活塞"

    # 發送HTTP請求並獲取響應
    response = requests.get(url)

    # 使用BeautifulSoup解析HTML響應
    soup = BeautifulSoup(response.content, "html.parser")

    # 找到所有包含太陽新聞的標題和連結
    o_news = []

    for tag in soup.find_all("li"):
        content = tag.a
        title_element = content.find("h2")
        if title_element:
            title = title_element.text
            thumbnail = content.find("img")["data-src"]
            article_link = content["href"]
            news_message = f"標題: {title}\n縮圖連結: {thumbnail}\n文章連結: {article_link}"
            o_news.append(TextSendMessage(text=news_message))

    # 如果找到新聞，就返回新聞訊息清單
    if o_news:
        return o_news
    else:
        # 如果找不到新聞，就返回一條訊息
        return [TextSendMessage(text="抱歉，找不到活塞最近的新聞。")]
    
def getpNews():
    # 定義要爬取的湖人新聞網頁URL
    url = "https://tw-nba.udn.com/search/tag/馬刺"

    # 發送HTTP請求並獲取響應
    response = requests.get(url)

    # 使用BeautifulSoup解析HTML響應
    soup = BeautifulSoup(response.content, "html.parser")

    # 找到所有包含太陽新聞的標題和連結
    p_news = []

    for tag in soup.find_all("li"):
        content = tag.a
        title_element = content.find("h2")
        if title_element:
            title = title_element.text
            thumbnail = content.find("img")["data-src"]
            article_link = content["href"]
            news_message = f"標題: {title}\n縮圖連結: {thumbnail}\n文章連結: {article_link}"
            p_news.append(TextSendMessage(text=news_message))

    # 如果找到新聞，就返回新聞訊息清單
    if p_news:
        return p_news
    else:
        # 如果找不到新聞，就返回一條訊息
        return [TextSendMessage(text="抱歉，找不到馬刺最近的新聞。")]
    
def getqNews():
    # 定義要爬取的湖人新聞網頁URL
    url = "https://tw-nba.udn.com/search/tag/國王"

    # 發送HTTP請求並獲取響應
    response = requests.get(url)

    # 使用BeautifulSoup解析HTML響應
    soup = BeautifulSoup(response.content, "html.parser")

    # 找到所有包含太陽新聞的標題和連結
    q_news = []

    for tag in soup.find_all("li"):
        content = tag.a
        title_element = content.find("h2")
        if title_element:
            title = title_element.text
            thumbnail = content.find("img")["data-src"]
            article_link = content["href"]
            news_message = f"標題: {title}\n縮圖連結: {thumbnail}\n文章連結: {article_link}"
            q_news.append(TextSendMessage(text=news_message))

    # 如果找到新聞，就返回新聞訊息清單
    if q_news:
        return q_news
    else:
        # 如果找不到新聞，就返回一條訊息
        return [TextSendMessage(text="抱歉，找不到國王最近的新聞。")]
    
def getrNews():
    # 定義要爬取的湖人新聞網頁URL
    url = "https://tw-nba.udn.com/search/tag/湖人"

    # 發送HTTP請求並獲取響應
    response = requests.get(url)

    # 使用BeautifulSoup解析HTML響應
    soup = BeautifulSoup(response.content, "html.parser")

    # 找到所有包含太陽新聞的標題和連結
    r_news = []

    for tag in soup.find_all("li"):
        content = tag.a
        title_element = content.find("h2")
        if title_element:
            title = title_element.text
            thumbnail = content.find("img")["data-src"]
            article_link = content["href"]
            news_message = f"標題: {title}\n縮圖連結: {thumbnail}\n文章連結: {article_link}"
            r_news.append(TextSendMessage(text=news_message))

    # 如果找到新聞，就返回新聞訊息清單
    if r_news:
        return r_news
    else:
        # 如果找不到新聞，就返回一條訊息
        return [TextSendMessage(text="抱歉，找不到湖人最近的新聞。")]
    
def getxNews():
    # 定義要爬取的湖人新聞網頁URL
    url = "https://tw-nba.udn.com/search/tag/黃蜂"

    # 發送HTTP請求並獲取響應
    response = requests.get(url)

    # 使用BeautifulSoup解析HTML響應
    soup = BeautifulSoup(response.content, "html.parser")

    # 找到所有包含太陽新聞的標題和連結
    x_news = []

    for tag in soup.find_all("li"):
        content = tag.a
        title_element = content.find("h2")
        if title_element:
            title = title_element.text
            thumbnail = content.find("img")["data-src"]
            article_link = content["href"]
            news_message = f"標題: {title}\n縮圖連結: {thumbnail}\n文章連結: {article_link}"
            x_news.append(TextSendMessage(text=news_message))

    # 如果找到新聞，就返回新聞訊息清單
    if x_news:
        return x_news
    else:
        # 如果找不到新聞，就返回一條訊息
        return [TextSendMessage(text="抱歉，找不到黃蜂最近的新聞。")]
    
def getyNews():
    # 定義要爬取的湖人新聞網頁URL
    url = "https://tw-nba.udn.com/search/tag/塞爾蒂克"

    # 發送HTTP請求並獲取響應
    response = requests.get(url)

    # 使用BeautifulSoup解析HTML響應
    soup = BeautifulSoup(response.content, "html.parser")

    # 找到所有包含太陽新聞的標題和連結
    y_news = []

    for tag in soup.find_all("li"):
        content = tag.a
        title_element = content.find("h2")
        if title_element:
            title = title_element.text
            thumbnail = content.find("img")["data-src"]
            article_link = content["href"]
            news_message = f"標題: {title}\n縮圖連結: {thumbnail}\n文章連結: {article_link}"
            y_news.append(TextSendMessage(text=news_message))

    # 如果找到新聞，就返回新聞訊息清單
    if y_news:
        return y_news
    else:
        # 如果找不到新聞，就返回一條訊息
        return [TextSendMessage(text="抱歉，找不到塞爾蒂克最近的新聞。")]
    
def getzNews():
    # 定義要爬取的湖人新聞網頁URL
    url = "https://tw-nba.udn.com/search/tag/溜馬"

    # 發送HTTP請求並獲取響應
    response = requests.get(url)

    # 使用BeautifulSoup解析HTML響應
    soup = BeautifulSoup(response.content, "html.parser")

    # 找到所有包含太陽新聞的標題和連結
    z_news = []

    for tag in soup.find_all("li"):
        content = tag.a
        title_element = content.find("h2")
        if title_element:
            title = title_element.text
            thumbnail = content.find("img")["data-src"]
            article_link = content["href"]
            news_message = f"標題: {title}\n縮圖連結: {thumbnail}\n文章連結: {article_link}"
            z_news.append(TextSendMessage(text=news_message))

    # 如果找到新聞，就返回新聞訊息清單
    if z_news:
        return z_news
    else:
        # 如果找不到新聞，就返回一條訊息
        return [TextSendMessage(text="抱歉，找不到溜馬最近的新聞。")]
    
def getaaNews():
    # 定義要爬取的湖人新聞網頁URL
    url = "https://tw-nba.udn.com/search/tag/雷霆"

    # 發送HTTP請求並獲取響應
    response = requests.get(url)

    # 使用BeautifulSoup解析HTML響應
    soup = BeautifulSoup(response.content, "html.parser")

    # 找到所有包含太陽新聞的標題和連結
    aa_news = []

    for tag in soup.find_all("li"):
        content = tag.a
        title_element = content.find("h2")
        if title_element:
            title = title_element.text
            thumbnail = content.find("img")["data-src"]
            article_link = content["href"]
            news_message = f"標題: {title}\n縮圖連結: {thumbnail}\n文章連結: {article_link}"
            aa_news.append(TextSendMessage(text=news_message))

    # 如果找到新聞，就返回新聞訊息清單
    if aa_news:
        return aa_news
    else:
        # 如果找不到新聞，就返回一條訊息
        return [TextSendMessage(text="抱歉，找不到雷霆最近的新聞。")]
    
def getbbNews():
    # 定義要爬取的湖人新聞網頁URL
    url = "https://tw-nba.udn.com/search/tag/暴龍"

    # 發送HTTP請求並獲取響應
    response = requests.get(url)

    # 使用BeautifulSoup解析HTML響應
    soup = BeautifulSoup(response.content, "html.parser")

    # 找到所有包含太陽新聞的標題和連結
    bb_news = []

    for tag in soup.find_all("li"):
        content = tag.a
        title_element = content.find("h2")
        if title_element:
            title = title_element.text
            thumbnail = content.find("img")["data-src"]
            article_link = content["href"]
            news_message = f"標題: {title}\n縮圖連結: {thumbnail}\n文章連結: {article_link}"
            bb_news.append(TextSendMessage(text=news_message))

    # 如果找到新聞，就返回新聞訊息清單
    if bb_news:
        return bb_news
    else:
        # 如果找不到新聞，就返回一條訊息
        return [TextSendMessage(text="抱歉，找不到暴龍最近的新聞。")]
    
def getccNews():
    # 定義要爬取的湖人新聞網頁URL
    url = "https://tw-nba.udn.com/search/tag/熱火"

    # 發送HTTP請求並獲取響應
    response = requests.get(url)

    # 使用BeautifulSoup解析HTML響應
    soup = BeautifulSoup(response.content, "html.parser")

    # 找到所有包含太陽新聞的標題和連結
    cc_news = []

    for tag in soup.find_all("li"):
        content = tag.a
        title_element = content.find("h2")
        if title_element:
            title = title_element.text
            thumbnail = content.find("img")["data-src"]
            article_link = content["href"]
            news_message = f"標題: {title}\n縮圖連結: {thumbnail}\n文章連結: {article_link}"
            cc_news.append(TextSendMessage(text=news_message))

    # 如果找到新聞，就返回新聞訊息清單
    if cc_news:
        return cc_news
    else:
        # 如果找不到新聞，就返回一條訊息
        return [TextSendMessage(text="抱歉，找不到熱火最近的新聞。")]
    
def getddNews():
    # 定義要爬取的湖人新聞網頁URL
    url = "https://tw-nba.udn.com/search/tag/獨行俠"

    # 發送HTTP請求並獲取響應
    response = requests.get(url)

    # 使用BeautifulSoup解析HTML響應
    soup = BeautifulSoup(response.content, "html.parser")

    # 找到所有包含太陽新聞的標題和連結
    dd_news = []

    for tag in soup.find_all("li"):
        content = tag.a
        title_element = content.find("h2")
        if title_element:
            title = title_element.text
            thumbnail = content.find("img")["data-src"]
            article_link = content["href"]
            news_message = f"標題: {title}\n縮圖連結: {thumbnail}\n文章連結: {article_link}"
            dd_news.append(TextSendMessage(text=news_message))

    # 如果找到新聞，就返回新聞訊息清單
    if dd_news:
        return dd_news
    else:
        # 如果找不到新聞，就返回一條訊息
        return [TextSendMessage(text="抱歉，找不到獨行俠最近的新聞。")]
    
def geteeNews():
    # 定義要爬取的湖人新聞網頁URL
    url = "https://tw-nba.udn.com/search/tag/爵士"

    # 發送HTTP請求並獲取響應
    response = requests.get(url)

    # 使用BeautifulSoup解析HTML響應
    soup = BeautifulSoup(response.content, "html.parser")

    # 找到所有包含太陽新聞的標題和連結
    ee_news = []

    for tag in soup.find_all("li"):
        content = tag.a
        title_element = content.find("h2")
        if title_element:
            title = title_element.text
            thumbnail = content.find("img")["data-src"]
            article_link = content["href"]
            news_message = f"標題: {title}\n縮圖連結: {thumbnail}\n文章連結: {article_link}"
            ee_news.append(TextSendMessage(text=news_message))

    # 如果找到新聞，就返回新聞訊息清單
    if ee_news:
        return ee_news
    else:
        # 如果找不到新聞，就返回一條訊息
        return [TextSendMessage(text="抱歉，找不到爵士最近的新聞。")]
    
def getffNews():
    # 定義要爬取的湖人新聞網頁URL
    url = "https://tw-nba.udn.com/search/tag/騎士"

    # 發送HTTP請求並獲取響應
    response = requests.get(url)

    # 使用BeautifulSoup解析HTML響應
    soup = BeautifulSoup(response.content, "html.parser")

    # 找到所有包含太陽新聞的標題和連結
    ff_news = []

    for tag in soup.find_all("li"):
        content = tag.a
        title_element = content.find("h2")
        if title_element:
            title = title_element.text
            thumbnail = content.find("img")["data-src"]
            article_link = content["href"]
            news_message = f"標題: {title}\n縮圖連結: {thumbnail}\n文章連結: {article_link}"
            ff_news.append(TextSendMessage(text=news_message))

    # 如果找到新聞，就返回新聞訊息清單
    if ff_news:
        return ff_news
    else:
        # 如果找不到新聞，就返回一條訊息
        return [TextSendMessage(text="抱歉，找不到騎士最近的新聞。")]
    
def getggNews():
    # 定義要爬取的湖人新聞網頁URL
    url = "https://tw-nba.udn.com/search/tag/鵜鶘"

    # 發送HTTP請求並獲取響應
    response = requests.get(url)

    # 使用BeautifulSoup解析HTML響應
    soup = BeautifulSoup(response.content, "html.parser")

    # 找到所有包含太陽新聞的標題和連結
    gg_news = []

    for tag in soup.find_all("li"):
        content = tag.a
        title_element = content.find("h2")
        if title_element:
            title = title_element.text
            thumbnail = content.find("img")["data-src"]
            article_link = content["href"]
            news_message = f"標題: {title}\n縮圖連結: {thumbnail}\n文章連結: {article_link}"
            gg_news.append(TextSendMessage(text=news_message))

    # 如果找到新聞，就返回新聞訊息清單
    if gg_news:
        return gg_news
    else:
        # 如果找不到新聞，就返回一條訊息
        return [TextSendMessage(text="抱歉，找不到鵜鶘最近的新聞。")]
    
def gethhNews():
    # 定義要爬取的湖人新聞網頁URL
    url = "https://tw-nba.udn.com/search/tag/籃網"

    # 發送HTTP請求並獲取響應
    response = requests.get(url)

    # 使用BeautifulSoup解析HTML響應
    soup = BeautifulSoup(response.content, "html.parser")

    # 找到所有包含太陽新聞的標題和連結
    hh_news = []

    for tag in soup.find_all("li"):
        content = tag.a
        title_element = content.find("h2")
        if title_element:
            title = title_element.text
            thumbnail = content.find("img")["data-src"]
            article_link = content["href"]
            news_message = f"標題: {title}\n縮圖連結: {thumbnail}\n文章連結: {article_link}"
            hh_news.append(TextSendMessage(text=news_message))

    # 如果找到新聞，就返回新聞訊息清單
    if hh_news:
        return hh_news
    else:
        # 如果找不到新聞，就返回一條訊息
        return [TextSendMessage(text="抱歉，找不到籃網最近的新聞。")]
    
def getiiNews():
    # 定義要爬取的湖人新聞網頁URL
    url = "https://tw-nba.udn.com/search/tag/魔術"

    # 發送HTTP請求並獲取響應
    response = requests.get(url)

    # 使用BeautifulSoup解析HTML響應
    soup = BeautifulSoup(response.content, "html.parser")

    # 找到所有包含太陽新聞的標題和連結
    ii_news = []

    for tag in soup.find_all("li"):
        content = tag.a
        title_element = content.find("h2")
        if title_element:
            title = title_element.text
            thumbnail = content.find("img")["data-src"]
            article_link = content["href"]
            news_message = f"標題: {title}\n縮圖連結: {thumbnail}\n文章連結: {article_link}"
            ii_news.append(TextSendMessage(text=news_message))

    # 如果找到新聞，就返回新聞訊息清單
    if ii_news:
        return ii_news
    else:
        # 如果找不到新聞，就返回一條訊息
        return [TextSendMessage(text="抱歉，找不到魔術最近的新聞。")]
