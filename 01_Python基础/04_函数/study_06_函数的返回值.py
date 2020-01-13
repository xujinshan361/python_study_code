def sum_2_num(num1, num2):
    """对俩个数字求和"""
    result = num1 + num2
    # 可以使用返回值，告诉调用函数一方计算的结果
    return result
    # return 表示返回，下方的代码不会被执行


print("计算结果：{0}".format(sum_2_num(10, 10)))
