import multiprocessing as mp

def job(x):
    print("In Job")
    return x*x

# 進程池Pool() 與map()
def multicore():
    """
    Pool 和之前的Process 的不同點是丢向Pool 的函數可以有返回值，而Process的没有返回值。
    """
    # 首先定義一個Pool
    # pool = mp.Pool()  #Pool 默認大小是CPU 的核數
    pool1 = mp.Pool()
    pool2 = mp.Pool(processes = 2)   # 自定義CPU 核數量為2

    # 使用map() 獲取结果，在map() 中需要放入函數和需要迭代運算的值，然後它會自動分配给CPU 核，返回结果。
    res = pool1.map(job, range(10))
    print(res)

    # apply_async() 為另一個可以返回結果的方法，但只能傳遞一個值，但是傳入值時要注意是可迭代的，所以在傳入值後需要加逗號，同时需要用get() 方法獲取返回值。
    # res = pool2.apply_async(job, (2,))
    # print(res.get())
    pool2.apply_async(job, (2,))

    # 使用apply_async() 輸出多個結果。
    multi_res =[pool2.apply_async(job, (i,)) for i in range(10)]
    print([res.get() for res in multi_res])


if __name__ == '__main__':
    multicore()