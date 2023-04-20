class Animal: # 含有抽象方法的叫抽象类
    def speak(self):
        pass   # 只有方法没有方法体，叫抽象方法，如果
class Dog(Animal):
    def speak(self):
        print("www")
class Cat(Animal):
    def speak(self):
        print("mmm")
# 多态：获得同一行为，不同状态
#              类型注解
def make_noise(animal:Animal):
    animal.speak()
dog = Dog()
cat = Cat()
make_noise(dog)
make_noise(cat)