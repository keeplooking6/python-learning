# 遍历输出字母
name = "wwwwxl"
for x in name:
    print(x)
print("------")
# range,前闭后开
for x in range(4):
    print(x,end=''+" ")
print()
for x in range(3,10):
    print(x,end=''+" ")
print()
for x in range(3,10,2):
    print(x,end=''+" ")
print()
# 99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}=",i*j,end=''+" ")
    print()

# 发工资案例
import random
money = 10000
for member in range(1,21):
    jiXiao = random.randint(1, 10)
    if(jiXiao < 5):
        print(f"第{member}号员工绩效太低，绩效为：{jiXiao},不发工资")
        continue
    else:
        print(f"给第{member}号员工发工资1000,绩效为：{jiXiao}")
        # money -= 1000
        if money <= 0:
            print("工资发完了，下月再发")
            break
print(money)