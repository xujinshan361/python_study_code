class Game(object):
    # 历史最高分
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("帮助信息：让僵尸进入大门")

    @classmethod
    def show_top_score(cls):
        print("历史记录： {0}".format(cls.top_score))

    def start_game(self):
        print("{0} 开始游戏了".format(self.player_name))


# 查看游戏的帮助信息
Game.show_help()
# 查看历史最高分
Game.show_top_score()
# 创建游戏对象
game = Game("小明")
game.start_game()

"""
小结：
实例方法        方法内部需要访问实例属性
类方法         方法内部只需要访问类属性
静态方法        方法内部不需要访问实例属性和类属性

如果需要访问类属性，也需要访问实例属性==>定义实例方法3
"""
