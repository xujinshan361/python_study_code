name_list = ["张三", "李四", "王五", "张三"]
# len(length 长度) 函数可以统计列表中元素的总数
list_len = len(name_list)
print("列表中包含{0}个元素".format(list_len))

# count 方法可以统计列表中某一个数据出现的次数
count = name_list.count("张三")
print("张三出现了{0}次".format(count))

# 从列表中删除数据,remove 只删除第一次出现的数据，如果数据不存在，会报错
name_list.remove("张三")
print(name_list)
