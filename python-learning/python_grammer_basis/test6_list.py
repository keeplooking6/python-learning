# 定义空列表
none_list = ()
none_list2 = list()
print(none_list)
print(none_list2)
# 定义列表字面量
# [1,2,"1"]

list = [1,2,3]
# print(list)

list1 = [[1,2,3],[4,5,6]]
# print(list1)

list2 = ["ttt",4,True]
# print(list2)

# 正序
print(list[0])
print(list[1])
# 二维数组
print(list1[0][0])
print(list1[0][1])
print(list1[1][0])
# 倒序
print(list2[-1])
print(list2[-2])

# 元素2在list中的位置（元素内容）
print(list.index(2))
# 修改某位置的元素数据（下标）
list[0] = 11
print(list)
list[-3] = 1
print(list)
# 在指定位置插入元素
list.insert(1,222)
print(list)
# 在末尾加入元素
print("在末尾加入元素")
list.append(444)
list.append(444)
print("在末尾加入元素")

print(list)
list.append([5,6,7])
print(list)
print("取出数组元素加入列表末尾")
# 末尾直接加入，而不是以一个数组作为一个元素的形式
# extend（容器） append（元素），即extend是将数据容器内的元素一个个取出再加入到列表中
list.extend([5,6,7])
print(list)
# 删除列表中的某元素（下标）
list.pop(2)
print(list)
del list[2]
print(list)
# 删除第一个匹配项
list.remove(444)
print(list)
# 清空某列表
print(list2)
list2.clear()
print(list2)
# 统计某元素在列表中的个数（元素内容）
print(list.count(5))
# 统计列表内有多少元素
print(len(list))

# practice
student_list = [21,25,21,23,22,20]
student_list.append(31)
print(student_list)
student_list.extend([29,33,30])
print(student_list)
print(student_list[0])
print(student_list[-1])
print(student_list.index(31))


# 遍历
list_even = [1,2,3,4,5,6,7,8,9,10,11]
index = 0
list_for_even_number = []
list_while_even_number = []
for x in list_even:
    if(x % 2 == 0):
        list_for_even_number.append(x)

while(len(list_even) > index):
    if(list_even[index] % 2 == 0):
        list_while_even_number.append(list_even[index])
    index += 1

print(list_for_even_number)
print(list_while_even_number)