# import time

# # nowTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# # print(nowTime)
# t1 = time.time()
# for i in range(10):
#     print(i)
# t2 = time.time()
# print(t2 - t1)

list = [1, 2, 3, 4, 5]
print("list[3:] :" + str(list[3:]))
print("list[6:] :" + str(list[6:]))

def func():
    return [lambda x: i*x for i in range(5)]

print([m(3) for m in func()])