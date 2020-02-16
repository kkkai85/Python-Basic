import numpy as np

print("A陣列")
A = np.arange(2, 14).reshape(3, 4)
print(A)
print(np.argmin(A)) # 取得矩陣最小值的索引
print(np.argmax(A)) # 取得矩陣最大值的索引

# 取得矩陣均值
print("矩陣平均值(average()):")
print(np.average(A))
print("矩陣平均值(mean()):")
print(np.mean(A))
# print("矩陣平均值(mean()):" + A.mean())

# 取得中位數
print("矩陣中位數(median()):")
print(np.median(A))

# 累加函數
print("累加函數:")
print(np.cumsum(A))

# 累差函數，計算每一行中後一項與前一項之差
print("累差函數:")
print(np.diff(A))

# 將所有非零元素的行與列座標分割開，重構成兩個分別關於行和列的矩陣
print(np.nonzero(A))

print("B陣列")
B = np.arange(14, 2, -1).reshape(3, 4)
print(B)
print("將每一行由小到大排序")
print(np.sort(B))