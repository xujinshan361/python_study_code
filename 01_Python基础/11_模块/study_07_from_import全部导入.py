from study_01_测试模块1 import *
from study_02_测试模块2 import *  # 会覆盖与模块1相同的函数和属性

print(title)
say_hello()

wangcai = Dog()
print(wangcai)
"""
相对于 import直接导入整个模块的好处，在使用函数时，不需要使用模块名
不推荐使用，容易出现问题，出现问题，很难解决
"""
