from pymongo import MongoClient

connect = MongoClient()

db = connect.Basic
coll = db.Basic_coll

# 查詢
# 注意以下方法均為只能使用一次，要輸出第二次就要重新find()
print("回傳一筆資料")
# 回傳一筆資料用find_one() 方法，回傳結果為字典型態
return_one = coll.find_one({'name':'kai'})
print(type(return_one))
print(return_one)
print(return_one["_id"])

print("回傳所有資料")
# 回傳所有資料用find() 方法
return_all = coll.find()
print(return_all)
for data in return_all:
	print(data)

# print("已列表型態輸出所有資料")
# return_all = coll.find()
# print(str(list(return_all)))

# return_data = [d for d in coll.find()]
# print(return_data)	