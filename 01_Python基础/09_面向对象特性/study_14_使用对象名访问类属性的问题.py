class Tool(object):
    # 使用赋值语句定义类属性，记录所有工具对象的数量
    count = 0

    def __init__(self, name):
        self.name = name
        # 让类属性的值+1
        Tool.count += 1


# 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("水桶")

# 输出工具数量
tool3.count = 99
# 注意: 如果使用 对象.属性 = 属性值 只会给对象添加一个属性，不会影响到类属性的值
# 不要用 对象.属性访问类属性， 该形式只能访问类属性，不能修改类属性，推荐使用
print(tool3.count)
print(Tool.count)

