# 隨機模組
import random

# 隨機選取
data = random.choice([1, 5, 6, 10, 20])		# 隨機選取一筆資料
data = random.sample([1, 5, 6, 10, 20], 3)		# 隨機選取三筆
print(data)

# # 隨機調換順序(就是洗牌的概念)
data = [1, 5, 8, 20]
random.shuffle(data)
print(data)

# 隨機取得亂數
data = random.random()	# 0 ~ 1 之間的隨機亂數
print(data)

data = random.uniform(0.0, 1.0)	# 0.0 ~ 1.0 之間的隨機亂數，0.0 與1.0 可修改決定開頭結尾
print(data)

# 取得常態分配亂數
data = random.normalvariate(100, 10)	# 100 中位數，10 標準差，得到的資料多數在90 ~ 110 之間
print(data)