import random

print(random.__file__)
rand = random.randint(0, 10)
print(rand)

"""
python 解释器在导入模块时，会：
搜索当前目录指定模块名的文件，如果有就直接导入，
如果没有，就在搜索系统目录

python 中每一个模块都有一个内置属性 __file__ ，可以查看模块的完整路径

"""
