hello_str = "hello word"

# 1.判断是否以指定字符串开始
print(hello_str.startswith("he"))

# 2.判断是否以指定字符串结束
print(hello_str.endswith("word"))

# 3.查找指定字符串
# index同样可以查找指定的字符串在大字符串中的索引
print(hello_str.find("lo"))
# index 如果指定的字符串不存在，会报错
# find如果指定的字符串不存在，会返回-1
# print(hello_str.index("abc"))
print(hello_str.find("abc"))

# 4.替换字符串
# replace 方法执行完成后，会返回一个新的字符串
# 注意：不会修改原有的字符串内容
print(hello_str.replace("word", "python"))
print(hello_str)
