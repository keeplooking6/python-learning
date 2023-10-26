# 判断数据是什么类型
print("判断数据是什么类型",end='')
print(type(1))

# int，str，list，tuple,dict,set都是type的实例
print("int，str，list，tuple,dict,set都是type的实例")
print(type(int))
print(type(list))
print(type(tuple))
print(type(str))
print(type(dict))
print(type(set))

print("object也是type的实例",end='')
# object也是type的实例
print(type(object))

print("type本身也是自己的实例",end='')
# type本身也是自己的实例
print(type(type))

print("Person,Student类的类型",end='')
class Person:
    pass
class Student(Person):
    pass

print(type(Student),end='')
print(type(Person))

print("stu实例的类型",end='')
stu = Student()
print(type(stu))
# print(stu)

print("person的__base__",end='')
print(Person.__bases__)
print("student的__base__",end='')
print(Student.__bases__)
# print(type())

