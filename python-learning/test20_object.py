# 对象的定义和使用
class student:
    name = None
    age = None
#     方法的定义和使用
    def getInfo(self):
        print(self.name)
        print(self.age)
# 类和对象 ：面向对象编程。类是设计图纸，对象的创建该实体
stu = student()
stu.name = "wxl"
stu.age = 19
stu.getInfo()
class clock:
    def ring(self):
        import winsound
        winsound.Beep(2000,3000)
clock1 = clock()
clock1.ring()
# __init__的使用
class stud():
    def __init__(self,name,age):
        self.name = name
        self.age = age
s = stud("wxl",11)
print(s.name)
print(s.age)

# practice
class class_student:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address
for x in range(2):
    print(f"当前录入第{x+1}位学生的信息")
    stu = class_student(input("学生姓名："),input("学生年龄："),input("学生地址："))
    print(f"学生x的信息录入完成，信息为：{stu.name},{stu.age},{stu.address}")
# 内置方法
class stu:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __lt__(self,other):
        return self.age < other.age
    def __le__(self, other):
        return self.age <= other.age
    # 大于等于
    # def __ge__(self, other):
    #     return self.age >= other.age
    # eq
    def __eq__(self, other):
        return self.age == other.age
    # 类似于java的tostring方法
    def __str__(self):
        return f"学生的姓名为:{self.name},年龄为:{self.age}"
stu1 = stu("wxl",12)
stu2 = stu("wdd",13)
# 本来是无法直接进行对象比较的，
print(stu1<stu2)
print(stu1>stu2)
print(stu1)


