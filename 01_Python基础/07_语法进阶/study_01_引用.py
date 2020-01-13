def test(num):
    print("在函数内部{0}，对应的内存地址是 {1}".format(num, id(num)))
    # 1>定义一个字符串变量
    result = "hello"
    print("函数要返回数据的内存地址是{0}".format(id(result)))
    # 2> 将字符串变量返回
    return result


# 1.定义一个数字的变量
a = 10
# 数据的地址本质上就是一个数字
print("a变量保存数据内存地址是 {0}".format(id(a)))

# 2.调用 test函数
# 注意：如果函数有返回值，但是没有定义变量接收，
# 程序不会报错，但是无法获取返回值结果
r = test(a)
print("{0}的内存地址是{1}".format(r, id(r)))
