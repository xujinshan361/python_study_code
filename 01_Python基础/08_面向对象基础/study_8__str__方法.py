class Cat:

    def __init__(self, new_name):
        self.name = new_name
        print("%s来了" % self.name)

    def __del__(self):
        """被动删除操作，当创建的对象从内存中删除的时候，会调用"""
        print("%s我去了" % self.name)

    def __str__(self):
        """必须返回一个字符串"""
        return "{0}  是小猫".format(self.name)


# tom 是一个全局变量
tom = Cat("Tom")
print(tom)
