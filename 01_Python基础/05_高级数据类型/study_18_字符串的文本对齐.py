# 假设：以下内容是从网上抓取的
# 要求：顺序并居中对齐输出以下内容
poem = ["\t\n登黄鹤楼",
        "王之涣",
        "白日依山尽\t\n",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]
for poem_str in poem:
    # 先使用strip方法去除字符串中的空白字幅
    # 再使用center 方法居中显示文本
    print("|{0}|".format(poem_str.strip().center(15, "　")))
