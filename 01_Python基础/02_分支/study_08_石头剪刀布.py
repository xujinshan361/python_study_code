# 导入随机工具包
# 注意：在导入工具包的时候，应该将导入的语句，放在文件的顶部
# 可以方便下面的代码，在任何需要的时候，使用工具包中的工具
import random

# 从控制台输入要出的拳----石头：1   剪刀：2   布：3
player = int(input("请输入要出的拳：(石头：1   剪刀：2   布：3):"))
# 电脑随机出拳
computer = random.randint(1, 3)
print("玩家出拳:{0},电脑出拳：{1}".format(player, computer))
# 比较胜负
"""
石头胜剪刀
剪刀胜布
布胜石头
if () or () or ():
通过（）可以将条件多行显示 
"""
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    print("恭喜玩家胜利！")
elif player == computer:
    # 平局
    print("平局")
    # 其他情况电脑获胜
else:
    print("玩家失败")
