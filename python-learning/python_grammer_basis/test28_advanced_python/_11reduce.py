#  reduce() 函数会对参数序列中元素进行累积操作
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# reduce只能处理一个序列
# 注意在 python2 和 python3 中，map/reduce/filter 的返回值类型有所不同，python2 返回的是基本数据类型，而 python3 则返回了迭代器。

from functools import reduce

def multiply(x):
    return (x * x)

def add(x):
    return (x + x)

funcs = [multiply, add]
for i in range(5):
    # reduce：将第一个数和第二个数进行相应处理，然后得到的结果在与第三个数进行相应处理
    value = reduce(lambda x,y:x(i)+y(i), funcs)
    print(value)
