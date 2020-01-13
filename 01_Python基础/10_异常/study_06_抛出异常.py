def input_password():
    # 提示用户输入密码
    pwd = input("请输入密码：")

    # 判断密码长度 >=8 返回用户输入的密码
    if len(pwd) >= 8:
        return pwd
    # 如果<8 主动抛出异常
    else:
        print("主动抛出异常")
        # 创建异常对象---可以使用错误信息字符串作为参数
        ex = Exception("密码长度不够")
        # 主动抛出异常
        raise ex


# 提示用户输入密码
try:
    print(input_password())
except Exception as result:
    print(result)
