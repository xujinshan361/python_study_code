xiaoming_dict = {"name": "小明",
                 "qq_number": "123456",
                 "phone": "10086"}
# 迭代器遍历字典
# 变量k是每一次循环中，获取到键值对的key
for k in xiaoming_dict:
    print("{0}---{1}".format(k, xiaoming_dict[k]))
