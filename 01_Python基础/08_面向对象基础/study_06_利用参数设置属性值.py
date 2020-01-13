class Cat:
    def __init__(self, new_name):
        print("这是一个初始化方法")
        # self.属性名 = 属性值
        # self.name = "Tom"
        self.name = new_name

    def eat(self):
        print("{0}爱吃鱼".format(self.name))


# 使用类名（）创建对象，会自动调用初始化方法__init__
tom = Cat("Tom")
tom.eat()
print(tom.name)

lazy_cat = Cat("lazy_cat")
lazy_cat.eat()
