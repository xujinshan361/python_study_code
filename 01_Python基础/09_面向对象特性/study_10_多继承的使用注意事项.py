class A:

    def test(self):
        print("A----test方法")

    def demo(selft):
        print("A----demo方法")


class B:

    def demo(self):
        print("B----demo方法")

    def test(self):
        print("B----test方法")


class C(A, B):
    """多继承，可以让子类对象，同时具有多个父类的属性和方法"""
    """A B 类都有的方法，先继承谁，子类就先继承谁的方法"""
    pass


# 创建子类对象
c = C()
c.demo()
c.test()

# 确定C类对象调用方法的顺序
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>) 按照元组的顺序查找执行
# Object 是所有类的基类
print(C.__mro__)
