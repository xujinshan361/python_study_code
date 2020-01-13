class Animal:

    def eat(self):
        print("吃---")

    def drink(self):
        print("喝---")

    def run(self):
        print("跑---")

    def sleep(self):
        print("睡---")


class Dog(Animal):

    def bark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):

    def fly(self):
        print("我会飞")

    def bark(self):
        # 针对子类中特有的需求，编写代码
        print("神一样的叫唤。。。")
        # 使用super()，调用原本在父类中封装的方法
        # 使用父类名.方法(self)  # 推荐使用
        # Dog.bark(self)  # 不推荐使用 一般Python2.7中使用

        # 注意：如果使用子类的调用方法，会出现递归调用--死循环！
        # XiaoTianQuan.bark(self)

        # super().bark()

        # 增加其他代码
        print("///////////////")


# 创建一个哮天犬的对象
xtq = XiaoTianQuan()
# 如果子类中重写了父类的方法
# 在使用子类对象调用方法时，会调用子类中重写的方法
xtq.bark()
