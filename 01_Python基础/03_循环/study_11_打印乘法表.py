# 打印输出9×9惩罚表
i, j = 1, 1
while i <= 9:
    j = 1
    while j <= i:
        print("{0}*{1}={2}".format(j, i, i * j), end="\t")
        j += 1
    print("")
    i += 1
