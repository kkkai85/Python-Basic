import json

"""
使用dumps()與loads()進行json資料基本讀寫，
dumps()是將Python中的文件序列化為json格式的str，
loads()是將已編碼的json字串解碼為Python物件。
"""

with open("jsonNote.json", "r") as file:
	# 將json字串解碼為Python物件
	jl = json.loads(file.read())

	print(jl)
	print(jl[0])
	print(len(jl))
	for i in jl:
		print(i['username'])

	# 將Python物件序列化為json格式
	jd = json.dumps(jl)
	print(jd)
	print(jd[0])
	print(len(jd))
	# for i in jd:
		# print(i['username'])
