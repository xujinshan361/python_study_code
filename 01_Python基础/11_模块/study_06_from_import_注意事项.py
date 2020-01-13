# from study_01_测试模块1 import say_hello
from study_02_测试模块2 import say_hello as module2_say_hello  # 给函数起别名
from study_01_测试模块1 import say_hello

# 从不同的模块中导入相同的函数，后导入的函数会把先导入的函数覆盖掉
say_hello()  # 调用模块1中的函数，直接调用
module2_say_hello()  # 调用模块2中的函数，可以使用别名
"""
从不同的模块中导入相同的函数，会执行后导入的函数
开发时 import 代码应该统一写在代码的顶部，更容易发生冲突
一旦发生冲突，可以使用 as关键字给其中一个工具起别名
"""
