def demo(*args, **kwargs):
    print(args)
    print(kwargs)


# 元组变量、字典变量
gl_nums = (1, 2, 3)
gl_dict = {"name": "小明", "age": 18}
# 会把gl_nums和gl_dict 作为元组传递给args
# demo(gl_nums,gl_dict)

# 拆包操作--简化元组变量、字典变量的传递
demo(*gl_dict, **gl_dict)
demo(1, 2, 3, name="小明", age=18)


"""
在调用多值函数时，如果希望：
将一个元组变量，直接传递给args
将一个字典变量，直接传递给kwargs

就可以使用拆包，简化参数的传递，拆包方式：
在元组变量前加一个*
在字典变量前加俩个**
"""