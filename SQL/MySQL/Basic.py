import pymysql

# 連接資料庫
# 1. connect = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='12345678', db='test', charset='utf8')
# 2. 
config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': 'kaijun945',
    'db': 'Test',
    'charset': 'utf8'
}
connect = pymysql.connect(**config)
"""
connect(**kwargs) 屬於connection 類的一個快捷函數，用於建構一個資料庫連接
**kwargs 參數說明如下:
host：主機名或 IP 地址（可选，默认为本地计算机）
port：連接MySQL / MariaDB資料庫使用的端口（可选，默认为3306）
database：連接的資料庫
user：連接資料庫的用戶
password：用戶的密碼
db：database参数的别名，用于兼容MySQLdb
passwd：password参数的别名，用于兼容MySQLdb
charset：資料庫操作使用的字符集，中文一般選擇utf8
"""

# 設定自動提交事務，或者在每次操作完成后手动提交事务conn.commit()
connect.autocommit(True)

# 設定游標
cur = connect.cursor()

# 建立資料庫(test)
create_database = "CREATE DATABASE IF NOT EXISTS test"
cur.execute(create_database)

# 刪除資料庫(test)
drop_database = "DROP DATABASE IF EXISTS test"
# cur.execute(drop_database)

# 查詢資料庫版本
cur.execute("SELECT VERSION()")
data = cur.fetchone()
print("Database version: %s" %data)

# 建立資料表(testable)
create_table = """CREATE TABLE IF NOT EXISTS testable(
    id      INT(5) PRIMARY KEY AUTO_INCREMENT,
    name    VARCHAR(20),
    age     INT(5),
    gender  CHAR(1)
)DEFAULT CHARSET = utf8
"""
cur.execute(create_table)

# 刪除資料表(testable)
drop_table = "DROP TABLE IF EXISTS testable"
# cur.execute(drop_table)

# 新增欄位(column)
create_column = "ALTER TABLE testable ADD phone CHAR(20)"
cur.execute(create_column)

# 刪除欄位
drop_column = "ALTER TABLE testable DROP phone"
cur.execute(drop_column)

# 新增(add)
create_data = "INSERT INTO testable(name, age, gender) VALUE(%s, %s, %s)"
data = {
    "name" : "Ann",
    "age" : "18",
    "gender" : "W"
}
cur.executemany(create_data, [(data["name"], data["age"], data["gender"])])

# 修改(update)
update_data = "UPDATE testable SET name = %s, age = %s, gender = %s WHERE id = 1"
new_data = {
    "name" : "Bob",
    "age" : "35",
    "gender" : "M"
}
cur.execute(update_data, [(new_data["name"], new_data["age"], new_data["gender"])])

# 刪除(delete)
delete_data = "DELETE FROM testable WHERE name = %s"
name = "Bob"
cur.execue(delete_data, [(name)])