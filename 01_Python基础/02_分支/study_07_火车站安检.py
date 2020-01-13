# 定义布尔类型变量 has_ticket 表示是否有车票
has_ticket = True

# 定义整形变量 knife_length  表示刀的长度，单位：厘米
knife_length = 30

# 首先检查是否有车票，如果有，才允许进行安检
if has_ticket:
    print("车票检查通过，进行安检！")
    # 安检时，需要检查刀的长度，判断是否超过20厘米
    if knife_length > 20:
        # 如果超过20厘米提示刀的长度，不允许上车
        print("刀超过长度，不允许上车！")
    # 如果不超过20厘米，安检通过
    else:
        print("安检通过！")
# 如果没有车票，不允许进门
else:
    print("没有车票，不允许进门！")
