hello_str = "hello hello"
# 统计字符串长度
print(len(hello_str))

# 统计某一个小字符串(子字符串)出现的次数
print(hello_str.count("he"))
# 如果统计的小字符串不存在，则返回0
print(hello_str.count("abc"))

# 某一子字符串出现的位置
print(hello_str.index("lo"))
# 如果使用index方法传递的子字符串不存在，则会报错
# print(hello_str.index("abc"))
