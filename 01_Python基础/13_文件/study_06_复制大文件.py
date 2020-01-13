# 1 打开
file_read = open("README")
file_write = open("READEM[复件]", "w")

# 2 读写
while True:
    text = file_read.readline()
    if not text:
        break
    file_write.write(text)

# 3 关闭
file_read.close()
file_write.close()
