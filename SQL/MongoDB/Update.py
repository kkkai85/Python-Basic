from pymongo import MongoClient

connect = MongoClient()

# 連接資料庫以及集合
db = connect.Basic
coll = db.Basic_coll

# 修改
value = {'name':'kai'}
newvalue = {"$set":{'name':'new kai'}}

print("修改一筆資料:")
# 修改一筆資料用update_one() 方法，但只能匹配到第一條紀錄
coll.update_one(value, newvalue)



print("修改多筆資料")
# 修改多筆資料用update_many() 方法，可以修改所有匹配到的紀錄
x = coll.update_many(value, newvalue)
x_get = coll.find(value)
print(x.modified_count, "筆資料已修改")

for x in coll.find():
	print(x)