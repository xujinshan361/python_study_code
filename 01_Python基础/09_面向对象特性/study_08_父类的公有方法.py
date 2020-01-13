class A:

    def __init__(self):
        self.num1 = 100
        self.__num2 = 200  # 私有属性

    def __test(self):
        print("私有方法{0}，{1}".format(self.num1, self.__num2))  # 私有方法

    def test(self):
        print("父类的公有方法 {0}".format(self.__num2))


class B(A):

    def demo(self):
        # 在子类的方法中不能访问父类的私有属性
        # print("访问父类的私有属性{0}".format(self.__num2))
        # 在子类的方法中不能调用父类的私有方法
        # self.__test()
        # 访问父类的公有属性
        print(self.num1)
        # 访问父类的公有方法
        self.test()
        pass


# 创建一个子类对象
b = B()
print(b)
# 在外界不能直接访问对象的私有属性和私有方法
# print(b.__num2)
# b.__test()

# 在外界访问父类的公有属性、调用公有方法
# print(b.num1)
# b.test()

b.demo()
