import threading
import time


def test01():
    for i in range(5):
        print("--------1------------")
        time.sleep(1)


def main():
    # 在调用之前先打印当前线程信息
    print(threading.enumerate())
    t1 = threading.Thread(target=test01)
    # 在调用thread之后打印
    print(threading.enumerate())

    t1.start()
    # 在调用start之后打印
    print(threading.enumerate())


"""当调用Thread的时候，不会创建线程"""
"""当调用Thread创建出来的实例对象的start方法时，才会创建线程已经让这个线程开始运行"""
if __name__ == "__main__":
    main()
