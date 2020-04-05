import numpy as np
import pandas as pd

# Pandas在基本資料結構上提供許多有用的工具、方法和功能，分別為Series、DataFrame和Index

"""
Series建構方式
pd.Series(data, index = index)
其中index為可選參數，可依照data型態決定使用
data為陣列或NumPy陣列時，index預設為整數序列。
data也可以是字典，其中index預設為排序的字典鍵
"""
print("Series基本使用")
nums = [0.5, 0.25, 0.7, 1.0, 2.1, 0.1]
pdata = pd.Series(nums)
print(pdata)
print(pdata.values)
print(pdata.index)
# 與Numpy類似，可使用相關索引搜索資料
print(pdata[1])
print(pdata[1:4])
print()

print("Series自定義索引與值相關聯")
pdata = pd.Series(nums, index = ["a", "b", "c", "d", "e", "f"])
print(pdata)
print(pdata["a"])
print()

print("Series當作特殊字典使用")
population = {
    "California" : 3925007,
    "Texas" : 27862596,
    "Florida" : 20612439,
    "New York" : 19745289,
    "Illinois" : 12801539
}
pdata = pd.Series(population)
print(pdata)
print(pdata["California"])
# 與字典不同，Series也可使用切片操作
print(pdata["California" : "New York"])
print()

"""
DataFrame建構方式
pd.DataFrame(data, columns = column_name,index = index)
"""
print("DataFrame基本使用")
area = {
    "California" : 423967,
    "Texas" : 695662,
    "New York" : 170312,
    "Florida" : 141297,
    "Illinois" : 149995
}
adata = pd.Series(area)
print(adata)
# DataFrame具有靈活列索引和靈活行名的二維陣列模擬，可以將DataFrame視為一系列對齊的Series物件
states = pd.DataFrame({"population" : pdata, "area" : adata})
print(states)
print(states.index)
print(states.columns)
# 可將DataFrame視為通用字典
print(states["area"])
print()

print("DataFrame進階使用")
# 單個Series物件製作DataFrame
print(pd.DataFrame(pdata, columns = ["population"]))
# 從字典串列製作DataFrame
print(pd.DataFrame([{"a" : i, "b" : i*2} for i in range(3)]))
print(pd.DataFrame([{"a" : 1, "b" : 2}, {"b" : 3, "c" : 4}]))
print(pd.DataFrame(np.random.rand(3, 2), columns = ["foo", "bar"], index = ["a", "b", "c"]))
print()

"""
DataFrame建構方式
pd.DataFrame(data, columns = column_name,index = index)
其中index為可選參數，可依照data型態決定使用
data為陣列或NumPy陣列時，index預設為整數序列。
data也可以是字典，其中index預設為排序的字典鍵
"""
print("Index基本使用")
# Index物件可以被認為是不可變陣列或有序集，在很多方面都像陣列一樣操作。
ind = pd.Index([2, 3, 5, 7, 11])
print(ind[1])
print(ind[:3])
print(ind[::2])
# Index物件也有許多NumPy陣列中的屬性。
print(ind.size, ind.shape, ind.ndim, ind.dtype)
# Index物件遵循set資料結構使用的許多約定，交集、聯集、差集和其他組合。
indA = pd.Index([1, 3, 4, 6, 7, 8])
indB = pd.Index([3, 5, 6, 8, 9, 11])
print(indA & indB) # 交集
print(indA | indB) # 聯集
print(indA ^ indB) # 差集
print()