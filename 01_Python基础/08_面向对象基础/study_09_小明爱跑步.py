class Person:
    def __init__(self, name, weight):
        # self.属性 = 形参
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字叫{0}，体重是{1}公斤".format(self.name, self.weight)

    def run(self):
        print("{0}爱跑步".format(self.name))
        self.weight -= 0.5

    def eat(self):
        print("{0}是吃货".format(self.name))

        self.weight += 1


xiaoming = Person("小明", 75.0)
xiaoming.run()
xiaoming.eat()

print(xiaoming)
