# 集合{}
print("集合Set 範例:")
s1 = {3, 4, 5}
print(s1)
print("10 in s1", 10 in s1)		
print("10 not in s1", 10 not in s1)

s2={4,5,6,7} 
s3=s1&s2 # 交集︰取兩個集合中，相同的資料
print(s3) 

s3=s1|s2 # 聯集︰取兩個合中的所有資料，但不重複取 
print(s3) 

s3=s1-s2 # 差集︰從 s1 中，減去和 s2 重疊的部分 
print(s3) 

s3=s1^s2 # 反交集︰取兩個集合中，重複的部分 
print(s3)

s=set("Hello") # 把字串中的字母折拆成集合︰ set(字串) 
print(s) 
print("H" in s) 
print("A" in s)

print("字典Dictionary 範例:")
# 字典{}
# 字典的運用︰key-value 配對 
dic={"apple":"蘋果","bug":"蟲蟲"} 
print(dic["apple"]) 

dic["apple"]="小蘋果" # 變更資料內容
print(dic["apple"]) 

dic={"apple":"蘋果","bug":"蟲蟲"} 
print("apple" in dic) # 判斷 key 是否存在 
print("test" in dic) 
print("test" not in dic) 
print(dic) 

del dic["apple"] # 刪除字典中的鍵值對 (key-value pair) 
print(dic) 

dic={x:x*2 for x in [3,4,5]} # 從列表的資料中產生字典 
print(dic)