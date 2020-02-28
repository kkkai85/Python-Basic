from bs4 import BeautifulSoup
from urllib import request
import requests

# 設定目標網址
base_url = "https://morvanzhou.github.io"
his = "/tutorials/data-manipulation/scraping/1-00-why/"
url = base_url + his

# 設定請求頭
header = { "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36" }

# 取得網址源碼，以及使用參數header 設置請求頭。
getUrl = requests.get(url, headers = header)
"""
getUrl.text 返回的是Unicode 的數據，getUrl.content 返回的是bytes 的數據。
若是想要取得文本內容(html)使用.text 方法。
若是想要取得圖片、文件，則使用.content 方法。
"""

# 舊方法為使用urlopen，但為了其他get、post等需求，所以使用requests 的套件為佳
res = request.urlopen(url)
html = res.read().decode('utf-8')
"""
request.urlopen("網址") 方法抓取網址內容。
使用read() 方法讀取網頁內容，使用decode('utf-8') 翻譯中文字。
"""

# 使用BeautifulSoup 解析網址源碼(html)內容，設置解析器為lxml。
soup = BeautifulSoup(getUrl.text, features = 'lxml')
"""
BeautifulSoup 主要使用find()、find_all()兩種方法取得網頁資訊。
.find_all(name = None, attrs = {}, recursive = True, text = None, limit = None, kwargs = '')，.find() 參數亦同。
可以直接挑選想要抓取的內容片段。
"""

# 使用find_all() 方法取得所有標籤img 且class = "course-image lazy-img"的資料內容。
all_img = soup.find_all("img", { "class" : "course-image lazy-img" })
for img in all_img:
    print(img)
    # 取得img 標籤內src 的內容。
    print(img["src"])

    # 下載圖片、文件，一樣使用get() 方法，參數設定stream 為True (預設為False)，將檔案分批下載。
    getImg = requests.get(base_url + img["src"], headers = header, stream = True)
    img_name = img["src"].split("/")[-1]
    with open("./img/%s" % img_name, "wb") as image:
        # 若文件記憶體不大，也可以不使用stream 直接下載。
        # image.write(getImg.content)

        # 使用iter_content(chunk_size) 來控制每個chunk 的大小，然後在文件中寫入chunk 大小的數據。
        for chunk in getImg.iter_content(chunk_size = 128):
            image.write(chunk)