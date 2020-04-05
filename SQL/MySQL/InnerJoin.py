import pymysql
import json

conn = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', password = '12345678', db = 'test', charset = 'utf8')
cur = conn.cursor()
conn.autocommit(True)


# 新建顧客資料表
cur.execute("DROP TABLE IF EXISTS c_table")
customer_table = """CREATE TABLE IF NOT EXISTS c_table(
    id	    INT(5),
    name	VARCHAR(30),
    age	    INT(5),
    phone	VARCHAR(11)
)DEFAULT CHARSET = utf8"""
cur.execute(customer_table)

# 將預設顧客資料存入資料表中
with open('E:/workspace/MySQL Note/Json File/customer.json', 'r', encoding = 'utf8') as file:
    customers = json.load(file)
    # print(type(customers))
    for customer in customers:
        create_data = "INSERT INTO c_table(id, name, age, phone) VALUE(%s, %s, %s, %s)"
        cur.executemany(create_data, [( customer['id'], customer['name'], customer['age'],customer['phone'] )])

# 新建訂單資料表
cur.execute("DROP TABLE IF EXISTS o_table")
order_table = """CREATE TABLE IF NOT EXISTS o_table(
    o_No	    INT(5),
    time	    VARCHAR(30),
    amount	    INT(5),
    c_id	        INT(5)
)DEFAULT CHARSET = utf8"""
cur.execute(order_table)

with open('./Json File/order.json', 'r', encoding = 'utf8') as file:
    orders = json.load(file)
    for order in orders:
        create_order = "INSERT INTO o_table(o_No, time, amount, c_id) VALUE(%s, %s, %s, %s)"
        cur.executemany(create_order, [( order['o_No'], order['time'], order['amount'], order['c_id'] )])

print("================================")
print("INNER JOIN")
inner_join = """
    SELECT o_table.o_No, c_table.name 
    # 選擇顧客名字和訂單編號，順序代表顯示資料的順序
    FROM c_table 	
    # 從顧客資料表
    INNER JOIN o_table
    # 與訂單資料表做交集
    ON c_table.id = o_table.c_id
    # 選取兩邊擁有相同c_id
"""
cur.execute(inner_join)
for data in cur.fetchall():
    print("訂單編號:", data[0], "顧客:", data[1])

print("================================")
print("LEFT JOIN")
left_join = """
    SELECT c_table.name, o_table.o_No
    FROM c_table
    LEFT JOIN o_table
    ON c_table.id = o_table.c_id
"""
cur.execute(left_join)
for data in cur.fetchall():
    print(data[0], "訂單編號:", data[1])


print("================================")
print("RIGHT JOIN")
right_join = """
    SELECT c_table.name, o_table.o_No
    FROM c_table
    RIGHT JOIN o_table
    ON c_table.id = o_table.c_id
"""
cur.execute(right_join)
for data in cur.fetchall():
    print(data[0], "訂單編號:", data[1])

print("================================")
print("ORDER BY")
order_by = """
    SELECT o_table.o_No, c_table.name, c_table.phone, o_table.amount
    FROM c_table
    INNER JOIN o_table
    ON c_table.id = o_table.c_id
    ORDER BY o_table.o_No
"""
cur.execute(order_by)
for data in cur.fetchall():
    print(data)