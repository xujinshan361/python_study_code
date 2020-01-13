import threading
import time


def test01():
    for i in range(5):
        print("---------test01------{0}".format(i))
        time.sleep(1)
    # 如果创建Thread时候执行的函数，运行结束，这个子线程就结束了


def test02():
    for i in range(5):
        print("---------test02------{0}".format(i))
        time.sleep(1)


def main():
    t1 = threading.Thread(target=test01)
    t2 = threading.Thread(target=test02)
    t1.start()
    t2.start()
    while True:
        print(threading.enumerate())
        if len(threading.enumerate()) <= 1:
            break
        time.sleep(1)


if __name__ == "__main__":
    main()
