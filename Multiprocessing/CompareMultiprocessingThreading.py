import multiprocessing as mp
import threading as td
import time

def square():
    for i in range(10000000):
        i += i**2

    print(i)

def square2(num):
    for i in range(num):
        i += i**2

    return i


if __name__ == '__main__':
    # 使用多進程multiprocessing
    t1_pro = time.time()
    pro1 = mp.Process(target = square)
    pro2 = mp.Process(target = square)
    pro1.start()
    pro2.start()
    pro1.join()
    pro2.join()
    t2_pro = time.time()
    print("multiprocessing:" + str(t2_pro - t1_pro))


    # 使用多進程map方法，用於需要迭代運算的值
    t3_pro = time.time()
    pl = mp.Pool(processes = 4)
    pro3 = pl.map(square2, (10000000, 10000000,))
    print(pro3)
    t4_pro = time.time()
    print("multiprocessing Pool:" + str(t4_pro - t3_pro))    

    # 使用多線程threading，thread 也可以使用multiprocessing 的Queue
    t1_thr = time.time()
    thr1 = td.Thread(target = square)
    thr2 = td.Thread(target = square)
    thr1.start()
    thr2.start()
    thr1.join()
    thr2.join()
    t2_thr = time.time()
    print("threading:" + str(t2_thr - t1_thr))

    # 兩者都不使用
    t1_nor = time.time()
    square()
    square()
    t2_nor = time.time()
    print("normal:" + str(t2_nor - t1_nor))