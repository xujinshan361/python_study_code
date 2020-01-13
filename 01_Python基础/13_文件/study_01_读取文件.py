# 1 打开文件--默认只读方式打开
file = open("README")  # 文件名区分大小写
# 2 读取文件内容
text = file.read()
print(text)

print("-" * 50)

# 3 关闭文件 -- 忘记关闭文件，会影响到后续文件的访问
file.close()
