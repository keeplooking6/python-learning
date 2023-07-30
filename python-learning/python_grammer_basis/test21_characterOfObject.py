# # # 私有方法
# class Phone:
#     IMEI = 123
#     producer = None
#
#     # __开头为私有变量，类对象无法调用
#     __current_voltage = None
#     def call_by_5g(self):
#         if self.__current_voltage and self.__current_voltage >= 1:
#             self.__keep_single_core()
#             print("5g童话已开启")
#         elif self.__current_voltage and self.__current_voltage < 1:
#             print("通话失败，电量不足")
#         else:
#             print("现在电量未知")
#
#     def __keep_single_core(self):
#         print("让CPU以单核模式运行以节省电量")
# # # 类对象无法调用私有变量
# # phone = Phone()
# # # phone.__keep_single_core # 报错,没有该方法
# # # print(phone.__current_voltage) #报错，没有该属性
# # # phone.__current_voltage = 33
# # # print(phone.__current_voltage) # 有值，但是新创建了一个变量，不是原有的私有变量了
# # # print(phone._Phone__current_voltage) #None
#
# # 继承
# class Phone2022(Phone):
#     IMEI = None
#     NFC = True
#     # 对父类不满意，子类可复写，方法，变量都可以复写
#     def call_by_5g(self):
#         print("5g童话已开启")
#         # 调用父类成员，两种方式
#         # 1
#         print("方式一：父类的IMEI=",super().IMEI)
#         print("父类的方法：")
#         super().call_by_5g()
#         # 2
#         print("方式二：父类的IMEI",Phone.IMEI)
#         Phone.call_by_5g(self)
# # 父类的非私有属性、方法都能被继承到
# new_phone = Phone2022()
# new_phone.call_by_5g()
# print("-----")
# print(new_phone.NFC)
# print("-----")
# print(new_phone.IMEI)
# print("-----")
# print(new_phone.call_by_5g())
# print("-----")
#
# class RemoteControl:
#     IMEI = 1000
#     print("远程红外线控制")
#
# # 多继承,继承优先顺序从左到右
# # 已经继承的子类，没办法写在多继承里
# class MyPhone(Phone,RemoteControl):
#     face_id = True
# my_new_phone = MyPhone()
# # 如果继承的两个类有相同变量，则起作用的是左侧的类变量(即phone的类变量）
# print(my_new_phone.IMEI)
#
# # pass关键字，保证函数或类定义的完整性，表示无内容或空
# class Nouse:
#     pass


# 注释中进行类型注解
import json
import random
var_1 = random.randint(2,6) # type: int
# 基础数据类型注解，一般无需注解，本来就知道是什么类型
var_2: int = 10
# 类对象类型注解
class student:
    print("学生")
stu = student()
stu: student
# 容器类型注解
# my_list: list=[1,2,3]
# my_dict: dict = {"姓名":"wxl"}
# my_tuple: tuple = ("sds",23,True)
# my_set: set = {1,2,3}
# 容器类型详细注解
# 下面这种，一般无需注解，本来就知道是什么类型
my_list: list[int] = [1,2,3]
# my_dict: dict[str,str]={"姓名":"wxl"}
my_tuple: tuple[str,int,bool] = ("sds",23,True)
my_set: set[int] = {1,2,3}
# 元组类型设置类型详细注解，需要将每一个元素都标记出来
# 字典类型设置类型详细注解，需要2个类型，第一个是key第二个是value

# 一般无法看出变量类型时才会添加类型注解
var_3: int = random.randint(2,6)
data = "{'e':'e'}"
var_4: dict = json.loads(data) # loads:字符串编程python数据类型
data2 = 14
def func(data2):
    return data2 * 10
var_5: stu = func(data2)

# 类型注解只做提示性作用，不会判断正误

# 对形参的注解
def add(x: int,y: int):
    return x+y
# 方法参数及返回值的注解
def func(data:list)->list:
    return data
