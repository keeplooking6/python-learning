# 最大元素
mystr = "itheima"
mylist = ("itheima",1,2)
mydict = {"key1":"value1","key2":"value2"}
myset = {"2vd",2,"ww"}
mytuple = {"1fe",23,2}

list_num = (11,1,2)
set_num = {1,2,13}
tuple_num = {22,23,2}

print(max(mystr)) # 字符串确定大小的规则
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
import random

list_classroom = [[],[],[]]
list_teacher = ['A','B','C','D','E','F','G','H']
for i in list_teacher:
    num = random.randint(0,2)
    list_classroom[num].append(i)
print(list_classroom)
