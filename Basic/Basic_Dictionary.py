print("字典Dictionary 範例:")
# 字典{}
# 字典的運用︰key-value 配對 
dic = {"apple":"蘋果","bug":"蟲蟲"} 
print(dic["apple"]) 

print("增加新的鍵值對")
dic["color"] = "green"
print(dic)

print("變更資料內容")
dic["apple"] = "小蘋果"
print(dic["apple"]) 

print("刪除字典中的鍵值對")
del dic["apple"]
print(dic) 

print("keys()方法返回字典的鍵")
dic = {"apple":"蘋果", "bug":"蟲蟲"} 
for key in dic.keys():
    print(key)

print("values()方法返回字典的值")
dic = {"apple":"蘋果", "bug":"蟲蟲"} 
for value in dic.values():
    print(value)

print("items()方法返回字典的鍵和值")
dic = {"apple":"蘋果", "bug":"蟲蟲"} 
for key, value in dic.items():
    print(key)
    print(value)

print("判斷字典中是否存在鍵或值")
# 判斷key是否存在 
print("apple" in dic)
print("apple" in dic.keys())
print("test" in dic) 
print("test" not in dic) 
# 判斷value是否存在
print("green" in dic.values()) 
print("green" not in dic.values())

# 使用get()方法判斷要檢索的值的鍵是否存在
"""
get()方法接受兩個參數
第一個為要搜尋的鍵
第二個為若該鍵不存在則返回的回應值
"""
val = dic.get("apple", "unknown")
print(val)
val = dic.get("color", "unknown")
print(val)
print(dic) 

# 使用setdefault()方法判斷要檢索的值的鍵是否存在
"""
使用setdefault()方法接受兩個參數
第一個為要搜尋的鍵
第二個為若該鍵不存在時，要設置在該鍵的值
"""
val = dic.setdefault("apple", "unknown")
print(val)
val = dic.setdefault("color", "green")
print(val)
print(dic) 

# 從列表的資料中產生字典 
dic = {x:x*2 for x in [3,4,5]}
print(dic)