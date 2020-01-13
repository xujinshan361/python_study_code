# 1 打开
file_read = open("README")
file_write = open("READEM[复件]", "w")

# 2 读写

text = file_read.read()
file_write.write(text)

# 3 关闭
file_read.close()
file_write.close()
