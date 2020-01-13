# 1.判断空白字幅
space_str = "   \t\n\r "
print(space_str.isspace())

# 2.判断字符串中是否只包含数字
# 1>都不能判断小数
# num_str = "1.1"

# 2>unicode 字符串
# num_str = "\u00b2"
# 3>中文数字
num_str = "一千零一"

print(num_str)
print(num_str.isdecimal())  # 如果string只包含数字则返回True，全角数字
print(num_str.isdigit())  # 如果string只包含数字则返回True，全角数字，（1），\u00b2
print(num_str.isnumeric())  # 如果string只包含数字则返回True，全角数字，汉字数字
