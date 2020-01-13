# 全局变量
num = 10


def demo1():
    # 希望修改全局变量的值
    # 在Python中，是不允许直接修改全局变量的值
    # 如果在使用赋值语句，会在函数内部，定义一个局部变量
    num = 99
    print("demo1==> {0}".format(num))


def demo2():
    print("demo2==> {0}".format(num))


demo1()
demo2()
