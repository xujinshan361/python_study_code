import study_01_测试模块1 as DogModule
import study_02_测试模块2 as CatModule  # 模块别名使用大驼峰原则

DogModule.say_hello()
CatModule.say_hello()

dog = DogModule.Dog()
print(dog)

cat = CatModule.Cat()
print(cat)
