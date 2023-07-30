# 最大元素
mystr = "itheima"
mylist = ("itheima",1,2)
mydict = {"key1":"value1","key2":"value2"}
myset = {"2vd",2,"ww"}
mytuple = {"1fe",23,2}

list_num = (11,1,2) #后续会转成列表
set_num = {1,2,13}
tuple_num = {22,23,2}

print(max(mystr)) # 字符串确定字母大小的规则
print(max(list_num))
print(max(mydict)) # 只对key进行排序
print(max(set_num))
print(max(tuple_num))
print("----")
print(min(mystr))
print(min(list_num))
print(min(mydict))
print(min(set_num))
print(min(tuple_num))
print("----")
# 类型转换
print(list(mydict))
print(type(list(mydict)))
print(set(mytuple))
print(type(set(mytuple)))
print(str(mytuple))
print(type(str(mytuple)))
# 排序：排序后都会得到list列表
print(sorted(tuple_num))
print(sorted(tuple_num,reverse =True)) # 默认false
# practice
# 1.幸运数字6：输入任意数字，如数字8，生成nums列表，元素值为1~8，从中选取幸运数字(能够被6整除)移动到新列表lucky，打印nums与lucky。
print("幸运数字：",end='')
nums = []
lucky = []
def generated_nums(num):
    i = 0
    while(i <= num):
        nums.append(i)
        i += 1
        if(i % 6 == 0):
            lucky.append(i)
generated_nums(int(input()))
print(nums)
print(lucky)
# practice2
# 2.列表嵌套：有3个教室[[],[],[]]，8名讲师['A','B','C','D','E','F','G','H']，将8名讲师随机分配到3个教室中
import random

list_classroom = [[],[],[]]
list_teacher = ['A','B','C','D','E','F','G','H']
for i in list_teacher:
    num = random.randint(0,2)
    list_classroom[num].append(i)
print(list_classroom)
