class Cat:
    def __init__(self):
        print("这是一个初始化方法")
        # self.属性名 = 属性初始值
        self.name = "Tom"


# 使类名（）创建对象的时候，会自动调用初始化方法 __init__
tom = Cat()
print(tom.name)
