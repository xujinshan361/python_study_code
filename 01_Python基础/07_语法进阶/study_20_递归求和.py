# 定义一个函数sum_number
# 能够接收一个numd 整数参数
# 计算1+2+3+...+num 的结果


def sum_number(num):
    # 1.出口
    if num == 1:
        return 1
    # 2.数字累加
    return num + sum_number(num - 1)


print(sum_number(100))
