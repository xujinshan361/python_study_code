file = open("README")
while True:
    text = file.readline()
    # 判断是否读取到文件内容
    if not text:
        break
    print(text, end="")  # 读取的时候已经有换行了，打印的时候不需要换行
file.close()
