# map:map(function_to_apply, list_of_inputs)
# function_to_apply：映射函数，也就是处理输入迭代类型的的每一个元素的函数。
# list_of_inputs：一个或多个序列。输入的序列类型：列表，集合，元组，字典及字符串。
# Map() 会根据提供的函数对指定序列做映射。
# 注意在 python2 和 python3 中，map/reduce/filter 的返回值类型有所不同，python2 返回的是基本数据类型，而 python3 则返回了迭代器。
def multiply(x):
    return (x * x)

def add(x):
    return (x + x)

funcs = [multiply, add]
for i in range(5):
    # map第一个参数，做一些相应处理的表达式，第二个参数：单个或多个序列
    value = map(lambda x:x(i), funcs)
    print(list(value))

with open('file.txt') as f:
    contents = f.read()

