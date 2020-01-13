class Gun:
    def __init__(self, model):
        # 枪的型号
        self.model = model
        # 子弹的数量
        self.bullet = 0

    def add_bullet(self, count):
        self.bullet += count

    def shoot(self):
        # 判断子弹数量
        if self.bullet <= 0:
            print("{0} 没有子弹了。。。".format(self.model))
            return
        # 发射子弹
        self.bullet -= 1
        # 提示发射信息
        print("{0}突突突。。。剩余子弹为{1}".format(self.model, self.bullet))


class Solider:
    def __init__(self, name):
        # 姓名
        self.name = name
        # 枪--新兵没有枪，先给赋值为空
        self.gun = None

    def fire(self):
        # 判断士兵是否有枪
        # is 判断是否在统一内存中
        # == 判断值是否相等
        if self.gun is None:
            print("{0} 还没有枪".format(self.name))
            return
            # 高喊口号
        print("冲啊冲啊。。。。{0}".format(self.name))
        # 让枪装填子弹
        self.gun.add_bullet(50)
        # 让枪发射子弹
        self.gun.shoot()


# 创建对象
ak47 = Gun("ak47")

# 创建新兵许三多
xusanduo = Solider("许三多")
xusanduo.gun = ak47
print(xusanduo.gun.model)
xusanduo.fire()
