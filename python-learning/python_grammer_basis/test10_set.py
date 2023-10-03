# 空集合定义
gather = set()
# 定义
gather2 = {"itheima","dd","dd",231,2,1,5,2}
print(gather)
# 定义集合字面量
# {1,2,"22s"}
# 无序去重输出
print(gather2)
gather2.add("w")
gather2.add(111)
print(gather2)
# 删除
gather2.remove("w")
print(gather2)
# 从集合中随机取出一个元素并删除
print(gather2.pop())
print(gather2.pop())
print(gather2.pop())
print(gather2)
# 清除集合
gather2.clear()
print(gather2)
# 对比集合的不同：集合1有而集合2没有的元素
gather3 = {1,2,3}
gather4 = {1,4,5}
print(gather3.difference(gather4))
print(gather3)
print(gather4)
# 更新不同的集合：集合1有，而集合2没有的元素，并将输出结果更新到集合1
gather3.difference_update(gather4) # 无返回值
print(gather3)
print(gather4)
# 合并不同的集合并去重
gather5 = gather3.union(gather4)
print(gather5)
print(gather3)
print(gather4)
# 长度
print(len(gather5))
# 只能使用for循环变脸，因为无序，无下标
for x in gather5:
    print(x)

print("-------")
# 集合的构造器永华
set2 = set(range(1, 10))
set3 = set((1,2,3))
set1 = {}
print("set1",set1)
print("set2",set2)
print("set3",set3)
# set1.add(4)
# set1.add(5)
# print("set1",set1)

set2.update([11, 12])
print("set2",set2)
# 删除元素5
set2.discard(5)
print("set2",set2)

if 4 in set2:
    set2.remove(4)
print(set1, set2)

