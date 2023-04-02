# 位置参数
def func1(name,age,sex):
    print(f"姓名：{name}，年龄：{age}，性别：{sex}")
print("位置参数")
func1("wxl",1,"女")
# 关键字参数key = value的值
print("关键字参数")
func1(age=12,sex="女",name="ww")
func1(age=12,sex="女",name="ww")
# 当只有部分关键字参数时，必须按参数位置照顺序写，且位置参数在前，关键字参数在后
func1("ww",age=12,sex="女")
# 缺省参数
print("缺省参数")
def func2(name,age,sex="女"):
    print(f"姓名：{name}，年龄：{age}，性别：{sex}")
func2("ww",22)
func2("ww",22,"男")
# 不定长参数
#   关键字传递
print("不定长参数-关键字传递：")
def func3(**args):
    print(args)
func3(name="ww",age=22)
#   位置传递
print("不定长参数-位置传递：")
def func3(*args):
    print(args)
func3("ww",22)

# 多个返回值
def add(x,y):
    z = x+y
    return x,y,z
print(add(11,2))
# 将函数作为参数传入:传递的是计算逻辑，而非数字
def test_func(compute):
    result = compute(1,2)
    print(result)
def compute(x,y):
    return x+y
test_func(compute)
# lambda函数:改写上述函数
def test_func(compute):
    result = compute(1,2)
    print(result)
test_func(lambda x,y:x+y) # 代表compute这个函数由lambda来写