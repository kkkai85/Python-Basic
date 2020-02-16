import threading

def thread_job(a):
    print(a)
    print("This is a added Thread, number is %s" % threading.current_thread())

if __name__ == '__main__':
    # 定義增加一個thread，名稱為T1，參數1
    add_thread = threading.Thread(target = thread_job, name = "T1", args = (1,))
    # 執行thread
    add_thread.start()

    # 顯示目前有幾個threading
    print(threading.active_count())
    # 顯目前激活的threading 名稱
    print(threading.enumerate())
    # 運行此程式的thread 名稱
    print(threading.current_thread())