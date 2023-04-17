# def sleep():
#     import random
#     import time
#     time.sleep(random.randint(1,5))
#     print("睡眠中。。。。")
#
# # 一般写法
# # print("我要睡觉")
# # sleep()
# # print("我要起床")
#
# # 闭包写法
# def outter(func):
#     def inner():
#         print("我要睡觉")
#         func()
#         print("我要起床")
#     return inner
# func = outter(sleep)
# func()

# 闭包的语法糖写法
def outer(func):
    def inner():
        print("我要睡觉")
        func()
        print("我要起床")
    return inner

@outer
def sleep():
    import random
    import time
    time.sleep(random.randint(1, 5))
    print("睡眠中。。。。")

sleep()
