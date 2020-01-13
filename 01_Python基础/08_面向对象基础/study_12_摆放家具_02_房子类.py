class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地 %.2f" % (self.name, self.area)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具名称列表
        self.item_list = []

    def __str__(self):
        # python 能够自动的将一对括号内部的代码链接到一起--对一行长的代码很有用
        return ("户型%s\n 总面积：%.2f 剩余：%.2f\n 家具：%s" %
                (self.house_type, self.area, self.free_area, self.item_list))

    def add_item(self, item):
        print("要添加 {0}".format(item))


# 创建家具

bad = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)
print(bad)
print(chest)
print(table)

# 创建房子
my_home = House("俩室一厅", 60)
my_home.add_item(bad)
my_home.add_item(chest)
my_home.add_item(table)
print(my_home)
