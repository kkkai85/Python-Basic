from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import os

# 若img 資料夾路徑不存在，則創建一個資料夾。
if not os.path.isdir("./img"):
    os.mkdir("./img")

# 取得目標網址，使用webdriver 開啟瀏覽器。
base_url = "https://morvanzhou.github.io"
home = "/learning-steps/"
url = base_url + home

driver = webdriver.Chrome('D:\Selenium Driver\chromedriver')
driver.get(url)

# 設定不打開瀏覽器也可運行webdriver
"""
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome('D:\Selenium Driver\chromedriver', chrome_options = chrome_options)
"""

# 控制滑鼠滾輪移動
"""
透過execute_script()執行js 代碼，控制網頁行動。
語法window.scrollBy(x, y)，參數(x, y)，向右向下滾動的像素質。
語法window.scrollTo(x, y)，參數(x, y)，視窗的(x, y)座標。
driver.execute_script("window.scrollBy(0, 2000)")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
"""

# 控制滑鼠點擊頁面
"""
driver.find_element_by_link_text("下一页").click()
"""

# 解析目標網址源碼，取得img 標籤的src 內容。
soup = BeautifulSoup(driver.page_source, features = 'lxml')
img = soup.find("img", {"class" : "lazy-img"})["src"]

# 重新組合目標網址，並下載該網址之內容，儲存為.png 檔案。
img_url = base_url + img
getImg = requests.get(img_url)
with open('./img/image1.png', 'wb') as f:
    f.write(getImg.content)

# 若目標檔案過大，可以將檔案分解成小部分逐一下載。
img_url = base_url + img
getImg = requests.get(img_url, stream = True)
with open('./img/image2.png', 'wb') as f:
    # 使用iter_content(chunk_size) 來控制每個chunk 的大小, 然後在文件中寫入這個chunk 大小的數據。
    for chunk in getImg.iter_content(chunk_size=32):
        f.write(chunk)