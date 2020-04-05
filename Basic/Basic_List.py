# 列表List[] 中括號，有順序、可動的列表
print("List[] 列表示範:")

grades = [12, 60, 15, 70, 90]

# 取得列表資料
print(grades)
print(grades[1])
print(grades[-2]) # 取得倒數第二筆資料
print(grades[1:4]) # 取得編號1 到編號4 (不包括)的資料
print(grades[:2])
print(grades[::2])

# 取得列表長度
print(len(grades)) 

# 取得列表中最大值
print(max(grades))
# 取得列表中最小值
print(min(grades))
# 取得列表中所有值的和
print(sum(grades))

# 統計某元素在列表中出現的次數
print(grades.count(60))

# 將列表進行排序
sorted_grades = sorted(grades)
print(sorted_grades)

# 使用sort()方法對List值進行排列
grades.sort()
print(grades)
# 使用reverse關鍵字，以使sort()按相反順序排列
grades.sort(reverse = True)
print(grades)

# 新增列表資料
grades.append(20)
print(grades)

# 變更列表資料
grades[0] = 55
print(grades)

grades = grades + [12, 33] # 將12，33加入列表後面
print(grades)

# 連續刪除編號1 到編號4 (不包括)的資料
grades[1:4] = []
print(grades)

# 刪除第二筆資料
grades = [12, 60, 15, 70, 90]
del grades[1]
print(grades)
grades.remove(90)
print(grades)

# List 搭配range() 使用
print(list(range(5)))
print(list(range(5, 10)))
print(list(range(5, 20, 3)))
print(list(range(30, 10, -3)))

# 列表也可以類似二維陣列或是三維陣列或更多，稱作巢狀列表