for num in [1, 2, 3]:
    print(num)
    if num == 2:
        break
else:
    # 如果循环体内部使用break退出了循环，则else不会执行
    print("会执行吗")

print("循环结束")
