import threading
import time

def T1_job():
    print("T1 start.")
    for i in range(10):
        # time.sleep(0.1)
        print("T1 " + str(i))
    print("T1 finish.")

def T2_job():
    print("T2 start.")
    for i in range(10):
        print("T2 " + str(i))

    print("T2 finish.")

if __name__ == '__main__':
    # 定義增加一個thread
    add_T1 = threading.Thread(target = T1_job, name = "T1")
    add_T2 = threading.Thread(target = T2_job, name = "T2")
    # 執行thread
    add_T1.start()
    add_T2.start()
    # 使用join 方法，限制等到add_thread 執行完成後才執行下面的語句
    add_T1.join()
    add_T2.join()

    print("All Done.")