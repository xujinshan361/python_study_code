# 使用多值参数
def sum_numbers(*args):
    num = 0
    print(args)
    # 循环遍历
    for i in args:
        num += i

    return num


# 使用元组参数
def sum_numbers2(args):
    num2 = 0
    print(args)
    for i in args:
        num2 += 1

    return num2


# 调用多值参数函数
result = sum_numbers(1, 2, 3, 4, 5)
print(result)
# 调用元组参数函数--需要俩个小括号
result2 = sum_numbers2((1, 2, 3, 4, 5))
print(result2)
