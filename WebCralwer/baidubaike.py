from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random

import pymongo

connect = pymongo.MongoClient()

db = connect.test
collect = db.ScrapingTest

base_url = "https://baike.baidu.com"
# history 用來存放爬過的網頁
his = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]


# url = base_url + his[-1]

# html = urlopen(url).read().decode('utf-8')
# print(html)
# soup = BeautifulSoup(html, features='lxml')
# soup.find() 方法會回傳第一個h1 標籤內容
# print(soup.find('h1').get_text(), '    url: ', his[-1])

for i in range(1, 6):
    url = base_url + his[-1]

    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, features='lxml')
    print(i, soup.find('h1').get_text(), '    url: ', url)

    data = {}
    data['Title'] = soup.find('h1').get_text()
    data['url'] = url
    collect.insert_one(data)

    # 觀察網站原始碼規律，尋找可以連結的網址
    sub_urls = soup.find_all("a", {"target": "_blank", "href": re.compile("/item/(%.{2})+$")})

    if len(sub_urls) != 0:
        his.append(random.sample(sub_urls, 1)[0]['href'])
    else:
        his.pop()