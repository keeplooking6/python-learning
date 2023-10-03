# set的pop是从随机取元素
set3 = {1,2,3}
print(set3.pop())
print(set3)

# list的pop是从后面出元素
list = [1,2,3]
print(list.pop())

# 遍历list(无序输出）
for i in list:
    print(i)
#  遍历tuple(有序输出）
tuple = (1,'ds',3)
for i in tuple:
    print(i)
#     遍历set(无序输出）
set = {10,"wd",11}
for i in set:
    print(i)
