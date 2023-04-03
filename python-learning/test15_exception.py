# 异常形式
try:
    # print(1/0)
    print("dd")
except(Exception) as e:
    print(e)
else:
    print("没有异常")
finally:
    print("有没有异常我都执行")