class Dog(object):

    # 不需要访问实例属性，也不需要访问类属性，可以使用静态方法，形参不需要第一个参数
    # 类方法第一个参数是cls ，实例方法第一个参数是self
    @staticmethod
    def run():
        print("小狗要跑。。。")


# 调用静态方法， 通过 类名.静态方法
Dog.run()
