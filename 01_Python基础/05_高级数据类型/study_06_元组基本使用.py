info_tuple = ("zhangsan", 18, 1.75, "zhangsan")

# 取值和取索引
print(info_tuple[0])  # 取值通过索引取出，索引从0开始，使用方括号
# 已经知道数据的内容，希望知道该数据在元组中的索引
print(info_tuple.index("zhangsan"))

# 统计计数
print(info_tuple.count("zhangsan"))

# 统计元组中包含元素的个数
print(len(info_tuple))
