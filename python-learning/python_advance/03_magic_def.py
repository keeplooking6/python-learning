class Student:
    def __init__(self,stu_list):
        self.person = stu_list
    #     使Student内部的数据可以被遍历
    def __getitem__(self, item):
        return self.person[item]
    # def __str__(self):
    #     return ",".join(self.person)

stu = Student(["qq","ww","ee"])
# 使用getitem
for s in stu:
    print(s)

# 使用str：qq,ww,ee
# print(stu)
# 不使用str：,默认调用__repr__
stu

class Num(object):
    def __init__(self,num):
        self.num = num
    def __abs__(self):
        return abs(self.num)

# 对类中的数据取绝对值
zheng_num = Num(-1)
print(abs(zheng_num))

# 只对一个num取绝对值
print(abs(-1))