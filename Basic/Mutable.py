a = "Hello"
b = "Python"
print(id(a), id(b))
a = "Hello"
b = "Hello"
print(id(a), id(b))
a += "Python"
print(id(a), id(b))
print(a, b)
b = a
print(id(a), id(b))
print(a, b)
b += "Good"
print(id(a), id(b))
print(a, b)

list1 = [1, 2, 3]
# list2 = [1, 2, 3]
list2 = list1
print(id(list1), id(list2))
# list2 = list1
# print(id(list1), id(list2))
list2.append(4)
print(id(list1), id(list2))
print(list1, list2)