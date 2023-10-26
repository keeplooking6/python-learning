# # # 闭包
# def outter(logo):
#     def inner(msg):
#         print(f"<{logo}>--{msg}--<{logo}>")
#     return inner
# # 调用outter函数，返回inner对象(return inner),即下面的fn返回的是inner函数，
# fn = outter("hm")
# # 然后这里是inner对象输入参数，输出内部信息
# fn("你想学什么")
#
# # atm例子
# def account_create(initial_amount = 0):
#     def atm(num,deposit = True):
#         nonlocal initial_amount
#         if deposit:
#             initial_amount += num
#             print(f"存款+{num},账户余额：{initial_amount}")
#         else:
#             initial_amount -= num
#             print(f"取款-{num},账户余额：{initial_amount}")
#     return atm
# money = account_create()
# money(100)
# money(100)
# money(100)
# money(100,deposit=False)

# def outter():
#     a = 101
#     def inner():
#         b = 202
#
#         # 带nonlocal，外部的a才可以被修改，不带nonlocal，外部的a不会改变
#         nonlocal a
#         a = b
#         print("a在inner中改变后：",a)
#     print("a执行inner前：",a)
#     inner()
#     print("执行inner后：",a)
#
# outter()

def outter():
    a = 101
    def inner():
        b = 202

        # 在闭包中global不会对外部的a起作用
        global a
        a = b
        print("a在inner中改变后：",a)
    print("a执行inner前：",a)
    inner()
    print("执行inner后：",a)

outter()

# 用global来修改函数外部的变量，但是函数外部的变量是可以被别的代码轻易识别到的，有篡改的风险
# 使用了闭包后，除非在函数内部本身将其变量值改变，别的代码调用是无法访问到函数内部的变量的。
# 达成了目的：既想使用外部变量，又不想外部变量被别的模块篡改