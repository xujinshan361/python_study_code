name_list = ["张三", "李四", "王五", "王小二"]

# 使用迭代器遍历列表
"""
顺序的从列表中依次获取数据，每一次循环过程中，数据都会保存在
my_name 这个变量中，，在循环体内部可以访问当前这一次获取的到的数据

for  循环内部使用的变量 in 列表：
    循环内部针对列表元素进行操作
    
    
"""
for my_name in name_list:
    print(my_name)
