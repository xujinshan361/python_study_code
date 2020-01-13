xiaoming_dict = {"name": "小明"}
# 取值
print(xiaoming_dict["name"])
# 在取值的时候，如果指定的key不存在，程序会报错
# print(xiaoming_dict["name123"])

# 增加、修改
# 如果key不存在，会新增键值对，如果key存在，会修改已经存在的键值对
xiaoming_dict["age"] = 18  # 增加

xiaoming_dict["name"] = "xiaoming"  # 修改

# 删除
xiaoming_dict.pop("age")
# 在删除指定键值对的时候，如果指定的key不存在，程序会报错
# xiaoming_dict.pop("age123")

print(xiaoming_dict)
