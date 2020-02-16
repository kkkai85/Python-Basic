import multiprocessing as mp
import threading as td

def job(a,d):
    print('aaaaa')

# 多進程Multiprocessing 與多線程threading 使用方法類似。
if __name__ == '__main__':
    t1 = td.Thread(target = job, args = (1,2))
    p1 = mp.Process(target = job, args = (1,2))

    t1.start()
    p1.start()

    t1.join()
    p1.join()