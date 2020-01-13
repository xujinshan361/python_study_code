def demo1():
    # 定义一个局部变量
    # 1> 出生：执行了下方的代码后，才会被创建
    # 2> 死亡：函数执行完成后
    num = 10
    print("在demo1函数内部的变量是{0}".format(num))


def demo2():
    num =99
    print(num)


# 在函数内部定义的变量，不能在其他位置使用
# print(num) # 不能访问
demo1()
demo2()