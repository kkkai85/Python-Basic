# Point 實體物件的設計: 平面座標上的點
class Point:
	# 定義初始化函式(方法)
	def __init__(self, x, y):
		self.x = x
		self.y = y

		# 定義實體方法
	def show(self):
		print(self.x, self.y)

	def distance(self, targetX, targetY):
		return (((self.x - targetX)**2) + ((self.y - targetY)**2))**0.5

# 可建立多個實體物件
p1 = Point(3, 4)
print(p1.x, p1.y)

p2 = Point(5, 6)
print(p2.x, p2.y)

p3 = Point(7, 8)
p3.show()	# 呼叫實體方法

result = p1.distance(0, 0)	# 計算座標(3, 4)和座標(0, 0)之間的距離
print(result)

# FullName 實體物件的設計: 分開紀錄姓、名資料的全名
class FullName:
	def __init__(self, firstname, lastname):
		self.firstname = firstname
		self.lastname = lastname

name1 = FullName("K.J.", "Zhan")
print(name1.firstname, name1.lastname)

name2 = FullName("W.C.", "Zeng")
print(name2.firstname, name2.lastname)