class Dog(object):

    def __init__(self, name):
        self.name = name

    def game(self):
        print("{0} 蹦蹦跳跳的玩。。。".format(self.name))


class XiaoTianQuan(Dog):

    def game(self):
        print("{0} 飞到天上去玩。。。".format(self.name))


class Person(object):

    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("{0} 和{1}快乐的玩耍。。。".format(self.name, dog.name))
        # 让狗玩耍
        dog.game()


# 创建一个狗对象
# wangcai = Dog("旺财")
wangcai =XiaoTianQuan("飞天旺财")
# 创建一个小明对象
xiaoming = Person("小明")

# 让小明调用和狗玩的方法
xiaoming.game_with_dog(wangcai)
