import pymysql

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': 'kaijun945',
    'db': 'Test',
    'charset': 'utf8'
}
connect = pymysql.connect(**config)
connect.autocommit(True)

cur = connect.cursor()

# 查詢敘述	使用子句要依照這個順序
# SELECT 	想要查詢的欄位
# FROM 		想要查詢的表格
# WHERE 	查詢條件
# GROUP BY	分組設定
# HAVING	分組條件
# ORDER BY	排序設定
# LIMIT		限制設定
# 查詢資料select 及其相關用法
# 查詢欄位:SELECT 欄位名稱(* 代表全部) FROM 資料表名稱
# 條件式查詢: SELECT 欄位名稱 FROM 資料表名稱 WHERE 條件式(例如: 參數 = %)
# 條件式可用and，or，between， 
# 查詢某一範圍 between: SELECT * FROM 資料表名稱 WHERE 欄位名 between 值1 and 值2;
# 查詢特定筆數: SELECT * FROM 資料表名稱 LIMIT 8, 10 (從第九筆開始選取10筆)
# 查詢結果遞增(減)排序: SELECT * FROM 資料表名稱 ORDER BY 欄位名(DESC)
# 查詢比對字串列出單一欄位: SELECT 欄位名 FROM 資料表名稱 WHERE 欄位名 LIKE "字串"
# 查詢比對字串列出所有欄位: SELECT * FROM 資料表名稱 WHERE 欄位名 LIKE "字串"

# 查詢
read_data = "SELECT * FROM testable"
data = cur.execute(read_data)
# 回傳table 資料筆數
print(data)

# 擷取第一行數據
# first_data = cur.fetchone()
# print(first_data)

# 擷取前n 行數據
# n = 3
# many_data = cur.fetchmany(n)
# print(many_data)

# 擷取所有數據
all_data = cur.fetchall()
print(all_data)