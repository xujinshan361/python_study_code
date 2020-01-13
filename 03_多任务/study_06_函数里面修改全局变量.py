num = 100
nums = [11, 22]

"""
在一个函数中对全局变量进行修改的时候，到底是否需要使用global进行说明，
要看是否对全局变量的指向进行了修改
如果修改了指向，让全局变量指向了一个新的地方，那么必须要使用global，
如果，仅仅是修改了指向的空间中的数据，此时不用必须使用global
"""


def test():
    global num
    num += 100
    nums.append(33)


print(num)
print(nums)
test()
print(num)
print(nums)
