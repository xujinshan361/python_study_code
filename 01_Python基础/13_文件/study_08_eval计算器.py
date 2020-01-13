input_str = input("请输入一个计算题：")
print(eval(input_str))
# 在开发时候，千万不要使用eval直接转换input的结果
# 如果输入参数类似：
# __import__('os').system("ls")
# 将可以处理任何终端命令
