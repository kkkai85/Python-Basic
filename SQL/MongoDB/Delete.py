from pymongo import MongoClient

connect = MongoClient()

# 連接資料庫以及集合
db = connect.Basic
coll = db.Basic_coll

# 刪除
print("刪除一筆資料")
# 刪除一筆資料用delete_one() 方法，第一個參數為查詢對象，指定要刪除那些數據
delete_data = {'name':'kk'}
coll.delete_one(delete_data)

for x in coll.find():
	print(x)



print("刪除多筆資料")
# 刪除多筆資料用delete_many() 方法
delete_datas = {"name":{"$regex":"^n"}} 	# 指定刪除n 開頭的資料
x = coll.delete_many(delete_datas)

print(x.deleted_count, "筆資料已刪除") 



print("刪除集合中所有資料")
# 若delete_many() 方法傳入為一個空的查詢對象，則會刪除集合中所有資料
x = coll.delete_many({})	
print(x.deleted_count, "筆資料已刪除")

# 刪除集合
# coll.drop()