# 1.提示用户输入苹果的单价
price = float(input("请输入苹果的价格："))

# 2.提示用户输入苹果的重量
weight = float(input("苹果的重量："))

# 3.计算金额
money = price * weight

print(money)

# 格式化输出
print("苹果的单价：{0},重量：{1},总金额:{2}".format(price, weight, money))
