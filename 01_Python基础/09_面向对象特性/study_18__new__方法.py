class MusicPlayer(object):

    def __new__(cls, *args, **kwargs):
        # 创建对象时候，new方法会被直接调用
        print("创建对象，分配空间")
        # 为对象分配空间
        # new 方法是静态方法 需要传递cls参数
        instance = super().__new__(cls)
        # 返回对象的引用
        return instance

    def __init__(self):
        print("播放器初始化")


# 创建播放器对象
player = MusicPlayer()

print(player)
