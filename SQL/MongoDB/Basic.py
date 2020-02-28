from pymongo import MongoClient

connect = MongoClient()
"""
# conn = MongoClient("<url>") 
# 如果要連接的資料庫是有權限密碼管制的，那就必須要在一開始做認證，只想連本機端的server 可以忽略
# 遠端的url填入: 
# mongodb://<user_name>:<user_password>@ds<xxxxxx>.mlab.com:<xxxxx>/<database_name>，
# 請務必既的把腳括號的內容代換成自己的資料
"""

# 連接資料庫
db = connect['Basic']
"""
# 連接到資料庫(Database)，若資料庫不存在則會創建一個，但資料庫只有在內容插入後才會創建
# 也就是說，創建資料庫後要創建集合(collection)，並插入一個文檔(紀錄)，資料庫才會真正創建
# db = connect.<database_name>	寫法一
# db = connect['database_name']	寫法二
"""

# 連接集合
collect = db.Basic_coll
"""
# 連接集合(collection)，若集合不存在則會創建一個，但集合只有在內容插入後才會創建...
# collect = db.<collection_name>
# collect = db['collection_name']
"""

# test if connection success
collect.stats  # 如果沒有error，就代表連線成功了。

# 插入一筆資料，創建新資料庫
collect.insert_one({'name':'new one'})

# 判斷資料庫以及集合是否存在
dblist = connect.list_database_names()
if "Basic" in dblist:
	print("資料庫Basic 建立成功!")

collectionlist = db.list_collection_names()
if "Basic_coll" in collectionlist:
	print("集合Basic_coll 建立成功!")