import pymysql
import json

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='12345678', db='test', charset='utf8')
cur = conn.cursor()
conn.autocommit(True)

# 載入json 檔案存到資料庫中
with open('./Json File/ex.json', 'r') as file:
	jf = json.loads(file.read())
	for line in jf:
		inesrt_re = "INSERT INTO testable(username, age, gender) VALUES (%s, %s, %s)"
		cur.executemany(inesrt_re, [(line['username'], line['age'], line['gender'])])