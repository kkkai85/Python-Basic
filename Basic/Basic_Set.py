# 集合Set{} 大括號，集合，無序、元素不重複
print("集合Set 判斷:")
s1 = {3, 4, 5}
s2 = {4,5,6,7} 
print("s1: ", s1)
print("s2: ", s2)
# 新增
s1.add(2)

# 新增多筆資料
s1.update({8, 9})
print("新增多筆資料", s1)

print("10 in s1", 10 in s1)		
print("10 not in s1", 10 not in s1)

# 交集︰取兩個集合中，相同的資料
print("交集: ", s1&s2) 

# 聯集︰取兩個合中的所有資料，但不重複取 
print("聯集: ", s1|s2) 

# 差集︰從 s1 中，減去和 s2 重疊的部分 
print("差集: ", s1-s2) 

# 反交集︰取兩個集合中，不重複的部分 
print("反交集: ", s1^s2) 

# 把字串中的字母折拆成集合︰ set(字串) 
s=set("Hello")
print(s) 
print("H" in s) 
print("A" in s)