# python中一切皆对象，函数，类都是对象
print("---python中一切皆对象，函数，类都是对象---")
def ask(name="wxl"):
    print(name)
my_ask = ask
# print(my_ask())是执行完的返回值
# print(my_ask) 是打印对象的地址
print(my_ask()) # 不写返回值，默认为none

class Person:
    def __init__(self):
        print("person")
my_person = Person
print("------")
print("---my_person---")
print(my_person) # 对象类型
print("---执行init中的内容:my_person(),无返回值，返回一个类对象---")
print(my_person()) # 执行init中的内容

print("---添加对象到列表---")
obj_list = []
obj_list.append(ask)
obj_list.append(Person)
for item in obj_list:
    print(item())

# 返回值可以是一个函数
print("---返回值可以是一个函数(装饰器原理）---")
def func():
    print("this is a function")
    return ask
# print(func()())
my_func = func()
print(my_func("tom"))
