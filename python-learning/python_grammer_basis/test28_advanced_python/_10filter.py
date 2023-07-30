# filter:第一个参数是函数处理，第二个参数是序列，序列中的元素经过第一个参数的函数处理后返回True或者False
# 返回True放入新的序列中
# filter只能处理一个序列
# 注意在 python2 和 python3 中，map/reduce/filter 的返回值类型有所不同，python2 返回的是基本数据类型，而 python3 则返回了迭代器。
def is_odd(n):
    return n % 2 == 1

tmplist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
newlist = list(tmplist)
print(newlist)
