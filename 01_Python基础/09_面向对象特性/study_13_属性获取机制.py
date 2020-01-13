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
print(Tool.count)
# tool1.count 对象.属性 查找顺序：先查找对象的属性，如果没找到，再向上找类的属性
# 不推使用
print(tool1.count)