# 几种命名tuple的方式
# 定义空元组
none_tuple = tuple()
none_tuple2 = ()
print(none_tuple)
print(none_tuple2)

tuple2 = (1,)
tuple3 = tuple2
print(tuple2)
print(tuple3)
# 存放不同的数据类型
tuple1 = (1,2,'ww','是',1,1,2)
# 中文 = 'e'
# print(中文)
print(tuple1)
# 某元素在元组中的位置
print(tuple1.index('ww'))
# 某元素在元组中的数量
print(tuple1.count(1))
# 支持嵌套
tuple5 = ((1,2,'s'),('w',2,3))
print(tuple5[1][0])
# 可以改变元组内的列表里的元素，但是不能把整个列表替换掉
tuple6 = (1,2,['s',12,'5wdw'])
tuple6[2][1] = 123
print(tuple6)
# practice
practice_tuple = ('zjl',11,['football','music'])
print(practice_tuple.index((11)))
print(practice_tuple[0])
practice_tuple[2].remove('football')
print(practice_tuple)
practice_tuple[2].append('coding')
print(practice_tuple)