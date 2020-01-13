# 1 打开文件--默认只读方式打开
file = open("README")  # 文件名区分大小写
# 2 读取文件内容
text = file.read()
print(text)
print(len(text))
print("-" * 50)

text = file.read()
print(text)

print(len(text))
# 3 关闭文件 -- 忘记关闭文件，会影响到后续文件的访问
file.close()

"""
文件指针 标记从哪个位置开始读取文件
第一次打开文件时，通常文件指针会指向开始位置
当执行了read方法后，文件指针会移动到读取文件的末尾
"""
