# 注意：在开发时，应该把模块中的所有全局变量
# 定义在所有函数上方，就可以保证所有的函数都能正常的访问到每一个全局变量
# 定义全局变量
num = 10


def demo():
    print("{0}".format(num))
    print("{0}".format(title))
    # print(name)        # 报错，会提示没有定义


# 再定义一个全局变量
title = "code"

demo()
# 再定义一个全局变量
name = "zhangsan "
