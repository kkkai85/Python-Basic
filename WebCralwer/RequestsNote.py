from bs4 import BeautifulSoup
import requests
import webbrowser

# 查詢參數
# param = {'q':'莫烦Python'}
# 使用get 方式下載普通網頁，將查詢參數加入get 請求中
# r = requests.get('https://www.google.com/search', params=param)

url = "https://www.youtube.com/results?"
header = { "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36" }
param = {'search_query':'iphone'}
r = requests.get(url, params = param, headers = header)
print(r.url)

# webbrowser.open(r.url)

# 取得網頁原始碼
# print(r.text)
# print(r.content)
# 網頁 url
# print(r.url)
# 取得網頁編碼
# print(r.encoding)
# 取得原始響應內容
# print(r.raw)

# 設置請求頭

# webbrowser.open(r.url)
# webbrowser.open(url, new=0, autoraise=True)
# 用默認瀏覽器打開url, new = 0是當前窗口, 1:新窗口, 2:新tab。
# autoraise 可能是自動切換到瀏覽器..測試無效. 最常用函数.


# 伺服器回應的狀態碼
print(r.status_code)


# 檢查狀態碼是否 OK
if r.status_code == requests.codes.ok:
	soup = BeautifulSoup(r.text, 'html.parser')

	items = soup.select('div.g > h3.r > a[href^="/url"]')

	for i in items:
		print("標題:" + i.text)

		print("網址:" + i.get('href'))