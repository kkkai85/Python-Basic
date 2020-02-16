# 統計模組
import statistics as stat
data = stat.mean([1, 2, 3, 4, 5, 8, 100])		# 計算列表中數字的平均數
print(data)

data = stat.median([1, 2, 3, 4, 5, 8, 100])		# 計算列表的中位數(去頭去尾取平均)
print(data)

data = stat.stdev([1, 2, 3, 4, 5, 8, 100])		# 計算列表的標準差
print(data)