f = open("txtFile.txt")
# f.seek(2) # 從文件第n個位元組開始讀取
r = f.read()
print(r)

L1 = r.split() # split()方法，按空格分離資料，得到一個字串
print(L1)

f.seek(0)
L2 = f.readlines()
print(L2)