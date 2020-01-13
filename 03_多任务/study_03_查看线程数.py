import threading
import time


def test01():
    for i in range(5):
        print("---------test01------{0}".format(i))


def test02():
    for i in range(5):
        print("---------test02------{0}".format(i))


def main():
    t1 = threading.Thread(target=test01)
    t2 = threading.Thread(target=test02)
    t1.start()
    time.sleep(1)
    print("--------1------")
    t2.start()
    time.sleep(1)
    print("-----------2--------")
    print(threading.enumerate())


if __name__ == "__main__":
    main()
