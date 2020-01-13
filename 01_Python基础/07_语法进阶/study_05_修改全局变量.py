num = 10


def demo1():
    # 希望修改全局变量的值---使用global 声明一下变量即可
    # global 关键字会告诉解释器后面的变量使用一个全局变量
    # 再使用赋值语句时，就不会创建局部变量
    global num
    num = 99
    print("demo1==> {0}".format(num))


def demo2():
    print("demo2==> {0}".format(num))


demo1()
demo2()