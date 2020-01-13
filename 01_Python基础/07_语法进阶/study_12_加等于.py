def demo(num, num_list):
    print("函数开始")
    # num = num + num  本质是赋值，函数内部操作，不会修改全局变量
    num += num
    # 列表变量使用+= 不会做相加再赋值的操作
    # 本质是调用列表的extend方法
    num_list.extend(num_list)
    num_list += num_list
    # 执行的是赋值操作，不会修改全局变量
    # num_list = num_list+num_list
    print(num_list)
    print(num)
    print("函数执行结束")


gl_num = 9
gl_list = [1, 2, 3]
demo(gl_num, gl_list)
print(gl_num)
print(gl_list)
