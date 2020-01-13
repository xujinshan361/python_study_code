class Cat:

    def __init__(self, new_name):
        self.name = new_name
        print("%s来了" % self.name)

    def __del__(self):
        """被动删除操作，当创建的对象从内存中删除的时候，会调用"""
        print("%s我去了" % self.name)


# tom 是一个全局变量
tom = Cat("Tom")
print(tom.name)

# del 关键字可以删除一个对象
del tom
print("-" * 20)
