name_list = ["张三", "李四", "王五"]
# 使用del关键字（delete）删除列表元素
# 提示：在日常开发中，要从列表删除数据，建议使用列表提供的方法
del name_list[1]

# del关键字本质上是用来将一个变量从内存中删除的
name = "小明"
del name  # 通过debug单步调试，可以看到是删除内存的操作
# 如果使用del关键字将变量从内存中删除，
# 后序的代码就不能再使用这个变量了
# print(name)

print(name_list)
