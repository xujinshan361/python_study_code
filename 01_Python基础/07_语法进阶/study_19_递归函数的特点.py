def sum_number(num):
    print(num)
    # 递归出口，当参数满足某个条件是，不再执行函数
    if num <= 0:
        return
    # 自己调用自己
    sum_number(num - 1)


sum_number(3)
