# while 迴圈
print("while 範例:")
n = 1
sum = 0
while n <= 10:
#	print(n)
	sum += n
	n += 1
print(sum)

while True:
	number = int(input('輸入數字：'))
	print('輸入數為', '奇數' if number % 2 else '偶數')
	if(input('繼續？（Yes/No）') == 'No'):
		break

# for 迴圈
print("for 範例:")
import sys
for arg in sys.argv:
	print(arg)

for x in [3, 5, 1]:
	print(x)

for x in "Hello":
	print(x)

for x in range(5): # range(5) 相當於[0, 1, 2, 3, 4]
	print(x)

for x in range(5, 10): # range(5, 10) 相當於[5, 6, 7, 8, 9]
	print(x)

for (x, y) in zip([1, 2, 3], [4, 5, 6]):
	print(x + y)

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
file = [d for d in data if d < 5]
print("file", file)

print("break 範例:")
# break
n = 0
while n < 5:
	n += 1
	if n == 3:
		break
	print(n)

print("continue 範例:")
# continue
for x in range(5):
	if x == 3:
		continue
	print(x)

print("else 範例解釋")
# else
sum = 0
for s in range(11):
	sum += s
else:
	print("for/while 迴圈結束前顯示")

print(sum)

# 綜合範例:找出整數平方根
num = int(input("請輸入一個正整數"))
for n in range(num):
	if n*n == num:
		print("整數平方根為" , n)
		break	# 用break 強制結束迴圈時，不會執行else 區塊
else:
	print("沒有整數平方根")