import multiprocessing as mp

def cube(q):
    for i in range(1000):
        i += i**3
    q.put(i)

if __name__ == '__main__':
    q = mp.Queue()
    pro = mp.Process(target = cube, args = (q,))
    pro.start()
    pro.join()

    res1 = q.get()
    print(res1)

    # res2 = q.get()
    # print(res2)