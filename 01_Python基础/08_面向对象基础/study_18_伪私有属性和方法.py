class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 18  # 属性前面加俩个 _(下划线) 表示私有属性

    def __secret(self):  # 方法前面加俩个下划线，表示私有方法
        # 在对象的方法内部，是可以访问对象的私有属性
        print("{0} 的年龄是{1}".format(self.name, self.__age))


xiaofang = Women("小芳")
# 伪私有属性在外界不能直接访问
print(xiaofang._Women__age)
# 伪私有方法在外界不能直接访问
xiaofang._Women__secret()
"""
python 没有真正的私有，只有伪私有属性和方法
在访问私有的时候，可以在属性和方法前面加 【下划线 类名 私有属性或方法】
开发时候不要使用
"""
