# 全局变量，函数，类，注意：直接执行的代码，不是向外界提供的工具
def say_hello():
    print("你好你好")


# 如果直接执行模块， __main__
if __name__ == "__main__":
    print(__name__)
    # 当文件被导入时候，能够被直接导入的代码不需要被直接执行
    print("小明开发的模块")
    say_hello()
