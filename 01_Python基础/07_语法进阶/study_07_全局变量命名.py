# 定义全局变量
gl_num = 10
gl_name = "xiaomin"


def demo():
    # 如果局部变量的名字和全局变量的名字相同
    # pycharm 会在局部变量下方显示一个灰色的虚线
    num = 99
    print(gl_num)
    print(gl_name)


demo()
