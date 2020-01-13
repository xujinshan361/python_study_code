i = 0
while i < 10:
    # continue 某一条件满足时，不执行后续重复代码
    # i==3
    if i == 3:
        # 注意在循环中，如果使用continue这个关键字时候
        # 需要确认循环的计数是否修改，
        # 否则可能导致死循环
        i += 19
        continue
    print(i)
    i += 1
