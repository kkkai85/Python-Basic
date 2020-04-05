# Python 只有if-else 判斷式，沒有switch-case
n1 = 10
n2 = 10
op = "-"
if op == "+": 
	print(n1 + n2) 
elif op == "-": 
	print(n1 - n2) 
elif op == "*": 
	print(n1 * n2) 
elif op == "/": 
	print(n1 / n2) 
else: 
	print("不支援的運算")

a = 2
b = 3
print("a < b") if a < b else print("a > b")