# 列表List 
print("List[] 列表示範:")
grades = [12, 60, 15, 70, 90]

print(grades) # 取得列表資料
print(grades[1]) # 取得列表內資料
print(len(grades)) # 取得列表長度 

grades[0] = 55 # 變更第一筆資料
print(grades)

print(grades[1:4]) # 取得編號1 到編號4 (不包括)的資料

grades[1:4] = [] # 連續刪除編號1 到編號4 (不包括)的資料
print(grades)

grades = grades + [12, 33] # 將12，33加入列表後面
print(grades)

# 列表也可以類似二維陣列或是三維陣列或更多，稱作巢狀列表

# 固定列表Tuple (操作與List 相同，但資料不可更動。)
print("Tuple() 列表示範:")
tupledata = (3, 4, 5)
print(tupledata)
# tupledata[0] = 55 # 因為不可更動，所以這行執行會發生錯誤
# tupledata[2] = [] # 不可更動、刪除