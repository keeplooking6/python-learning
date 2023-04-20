num = 11
# 字符串类型无法和其他类型拼接
print("11",num,"www")
str = "ww"
print("sss"+str)
# 精度控制
num = 11.3
print("数字为：%f" %num)
print("数字为：%4.2f" %num)
# 快速格式化
print(f"我的数字为：{num}")
# 表达式格式化
print("表达式格式化:%d" %(2*3))
print(f"表达式格式化:{3*3}")
print("表达式格式化:%s" %type("hello"))
# 计算股价小程序
name = "传播智客"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_days = 7
finally_storck_price = stock_price*stock_price_daily_growth_factor**growth_days
print(f"公司：{name},股票代码：{stock_code},当前股价：{stock_price}")
print("每日增长系数是：%.1f,经过%d天的增长后，股价达到了:%.2f"%(stock_price_daily_growth_factor,growth_days,finally_storck_price))
# 数据输入
name = input("请问你的名字是？")
print("get,我知道你叫%s" %name)
# 登录小程序
user_name = input("用户名：")
user_type = input("用户类型：")
print(f"您好，{user_name},您是尊贵的：{user_type}用户，欢迎您的光临")
