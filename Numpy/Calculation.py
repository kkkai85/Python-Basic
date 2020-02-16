import numpy as np

a = np.array([10, 20, 30, 40])
b = np.arange(4)

c = a + b 
c = a - b
c = a * b
c = b **2
c = 10 * np.sin(a)
print(c)

print(b < 3)

a=np.array([[1,1],[0,1]])
b=np.arange(4).reshape((2,2))

print(a)
# array([[1, 1],
#       [0, 1]])

print(b)
# array([[0, 1],
#       [2, 3]])

# 矩陣乘法
c_dot = np.dot(a,b)
print(c_dot)
# array([[2, 4],
#       [2, 3]])
c_dot_2 = a.dot(b)
# array([[2, 4],
#       [2, 3]])

a = np.random.random((2, 4))
print(a)

print(np.sum(a))
print(np.max(a))
print(np.max(a, axis = 1)) # axis 為1的時候，以行為單位查找
print(np.max(a, axis = 0)) # axis 為0的時候，以列為單位查找
print(np.min(a))