print("Hello Python")

import sys

print('Hello ' + sys.argv[0] + ' !')
# sys.argv 使用者輸入的命令列引數，會收集為字串陣列並給sys.argv參考，
# 索引0是啟動的模組名稱，之後則陸續是使用者所輸入的引數。
# 只能用命令提示字元來操作

name = input("請輸入你的名字:")
print("Hello " + name)

# # input() 可以取得使用者的輸入，也可以指定提示文字，
# 使用者輸入的文字則以字串傳回。