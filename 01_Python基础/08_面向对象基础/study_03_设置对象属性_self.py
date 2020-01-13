class Cat:
    """猫类"""

    def eat(self):
        # 哪一个对象调用的方法，self就是哪一个对象的引用
        print("{0}爱吃鱼".format(self.name))

    def drink(self):
        print("{0}要喝水".format(self.name))


# 创建对象
tom = Cat()

# 可以使用 . 属性名     利用赋值语句就可以了
# 这种方式简单，但是不推荐使用
tom.name = "Tom"

tom.eat()
tom.drink()
print(tom)
print(tom.name)

# 再创建一个对象
lazy_cat = Cat()
lazy_cat.name = "大懒猫"
lazy_cat.eat()
lazy_cat.drink()
