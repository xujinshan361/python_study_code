def print_info(name, title="学生", gender=True):
    """打印信息

    :param title: 职位
    :param name: 班上同学的姓名
    :param gender: True:男生   False:女生
    """
    gender_text = "男生"
    if not gender:
        gender_text = "女生"

    print("【{2}】{0} 是 {1}".format(name, gender_text, title))


# 假设班上的同学男生居多！
# 提示：在指定缺省参数的默认值时，应该使用最常见的值作为默认值！
print_info("小明")
print_info("老王", gender=False)
