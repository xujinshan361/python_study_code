try:
    # 提示用户输入一个整数
    num = int(input("输入一个整数："))
    # 使用 8 除以用户输入的整数并且输出
    result = 8 / num
    print(result)
except ValueError:
    print("请输入正确的整数")
# 捕获未知异常，打印输出---便于查找异常
except Exception as result:
    print("未知错误 {0}".format(result))
else:
    # 尝试执行的代码没有出现异常的情况下才会被执行
    print("尝试成功")
finally:
    # 无论是否出现错误，都能被执行
    print("无论是否出现错误都会执行的代码")
print("*" * 50)
