class Tool(object):
    # 使用赋值语句定义类属性，记录所有工具对象的数据
    count = 0

    def __init__(self, name):
        self.name = name

        # 让类属性值+1
        Tool.count += 1

    @classmethod
    def show_tool_count(cls):
        print(cls.count)


# 创建工具对象
tool1 = Tool("斧头")
tool = Tool("锄头")

# 调用类方法
Tool.show_tool_count()
