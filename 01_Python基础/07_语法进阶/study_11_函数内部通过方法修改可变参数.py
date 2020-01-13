def demo(num_list):
    print("函数内部的代码")
    # 使用方法修改列表的内容
    # 注意：如果传递的参数是可变类型，在函数内部，使用方法修改数据的内容，同样会影响到外部的数据
    num_list.append(9)
    print(num_list)
    print("函数执行完成")


gl_list = [1, 2, 3]
demo(gl_list)
print(gl_list)
