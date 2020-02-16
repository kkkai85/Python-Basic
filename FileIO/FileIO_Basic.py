# 儲存檔案
# 檔案操作流程: 開啟檔案 > 讀取或寫入 > 關閉檔案
# 基本語法: 檔案物件 = open(檔案路徑, mode = 開啟模式)
# file.open("data.txt", mode = "w", encoding = "UTF-8")	
# 開啟，使用utf-8 才能夠寫入(讀取)中文字
# file.write("Write File\n進入第二行")	# 操作
# file.close()	# 關閉

# 最佳實務，以下區塊會自動、安全的關閉檔案。
with open("data.txt", mode = "w", encoding = "UTF-8") as file:
	file.write("5\n3")

# 讀取檔案
sum = 0
with open("data.txt", mode = "r", encoding = "UTF-8") as file:
    # content = file.read()	# 一次讀取全部檔案內容
	for line in file:	# 將檔案一行一行讀取
		sum += int(line)
#print(content)
print(sum) 

# 使用JSON 格式讀取、複寫檔案
import json
with open("config.json", mode = "r") as file:
	data = json.load(file)
print(data)	# data 是一個字典資料。
# print("name", data["name"])
# print("id", data["id"])
data["name"] = "New Name"	# 修改變數中的資料

# 將更新資料複寫到.json 檔案中
with open("config.json", mode = "w") as file:
	json.dump(data, file)