class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 18  # 属性前面加俩个 _(下划线) 表示私有属性

    def __secret(self):  # 方法前面加俩个下划线，表示私有方法
        # 在对象的方法内部，是可以访问对象的私有属性
        print("{0} 的年龄是{1}".format(self.name, self.__age))


xiaofang = Women("小芳")
# 私有属性在外界不能直接访问
# print(xiaofang.__age)
# 私有方法在外界不能直接访问
# xiaofang.__secret()
