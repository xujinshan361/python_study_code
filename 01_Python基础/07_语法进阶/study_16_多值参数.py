def demo(num, *nums, **person):
    print(num)
    print(nums)
    print(person)


# demo(1)
demo(1, 2, 3, 4, 5, name="小明", age=18)
"""
python 中有俩种多值参数
1>参数前面加一个 *  可以接收元组
2>参数前面加俩个 ** 可以接收字典

一般给多值参数命名时，习惯使用以下俩个名字
*args   --可以存放元组
**kwargs  --可以存放字典
"""