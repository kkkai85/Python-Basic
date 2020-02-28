from pymongo import MongoClient

connect = MongoClient()

db = connect.Basic
coll = db.Basic_coll

# 新增
# 插入文檔時第一個參數預設為_id，若沒有指定_id 值，MongoDB 會為每個文檔自動添加唯一的id
print("新增一筆資料")
# 集合中插入一筆文檔用insert_one() 方法，參數為字典的型態
data_dict = {'name':'kai', 'age':20, 'gender':'male'}
x = coll.insert_one(data_dict)	# 插入一筆資料data_dict
# insert_one() 方法返回InsertOneResult 對象，該對象包含inserted_id 屬性，它是插入文檔的id 值
print(x.inserted_id)	# 輸出插入的資料的id 值

print("新增多筆資料")
# 集合中插入多筆文檔用insert_many() 方法，參數為字典列表的型態
data_list = [
	{
		'name':'kai',
		'age':22,
		'gender':'male'
	},
	{
		'name':'wei',
		'age':23,
		'gender':'female'
	},
	{
		'name':'kk',
		'age':20,
		'gender':'male'
	}
]
y = coll.insert_many(data_list)
print(y.inserted_ids)	# 輸出插入的所有文檔的_id 值