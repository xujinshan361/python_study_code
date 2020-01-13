students = [
    {"name": "张三"},
    {"name": "李四"}
]

# 在学员列表中搜索指定的姓名
find_name = "张三2"
for stu_dict in students:
    print(stu_dict)
    if stu_dict["name"] == find_name:
        print("查找到了{0}".format(find_name))
        # 如果找到了，应该直接退出循环，而不再遍历后序的元素
        break
else:
    print("没有找到")
print("循环结束")
