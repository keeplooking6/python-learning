# # 闭包
# def outter(logo):
#     def inner(msg):
#         print(f"<{logo}>--{msg}--<{logo}>")
#     return inner
# # 调用outter函数，返回inner对象(return inner),即下面的fn返回的是inner函数，
# fn = outter("hm")
# # 然后这里是inner对象输入参数，输出内部信息
# fn("你想学什么")

# atm例子
def account_create(initial_amount = 0):
    def atm(num,deposit = True):
        nonlocal initial_amount
        if deposit:
            initial_amount += num
            print(f"存款+{num},账户余额：{initial_amount}")
        else:
            initial_amount -= num
            print(f"取款-{num},账户余额：{initial_amount}")
    return atm
money = account_create()
money(100)
money(100)
money(100)
money(100,deposit=False)
