# 打印5遍 hello python
# 1.定义一个整形变量，记录循环的次数
i = 0
# 2.开始循环
while i < 5:
    # 1>希望在循环内部执行的代码
    print("hello python")
    # 2>处理计数器
    # i=i+1
    i += 1
# 3.观察以下，循环结束后，计数器i的数值是多少
print("循环结束后：i={0}".format(i))
