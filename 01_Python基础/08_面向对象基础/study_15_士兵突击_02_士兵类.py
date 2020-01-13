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


# 创建对象
ak47 = Gun("ak47")
ak47.add_bullet(50)
ak47.shoot()

# 创建新兵许三多
xusanduo = Solider("许三多")
xusanduo.gun = ak47
print(xusanduo.gun.model)
