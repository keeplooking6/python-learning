# # 成年人判断
print("欢迎来到黑马儿童游乐场，儿童免费，成人收费")
age = int(input("请输入你的年龄："))
if age < 18:
    print("您未成年不需要买门票")
else :
    print("您已成年，游玩需门票30元")
print("祝您玩得愉快")

# 猜猜心里的数字
import random
num = random.randint(1,10)
i = 0
while i<3:
    guess = int(input("请输入第一次猜想的数字："))
    if(1 <= guess <= 10):
        if(guess < num):
            print("不对，太小了")
        elif(guess > num):
            print("不对，太大了")
        else:
            print("回答正确")
            exit()
    else:
        print("应该猜1-10以内的数字")
    i += 1

# 1-100累加的和
sum = 0
i = 1
while(i <= 100):
    sum += i
    i += 1
print(sum)

# 99乘法表
num1 = 1
num2 = 1
while(num1 <= 9):
    while(num2 <= num1):
        print(f"{num2}*{num1} =",num1 * num2,"\t",end='')
        num2 += 1
    num1 += 1
    num2 = 1
    print()
# \t
print("hello\tworld")
print("wwwwww\twww")

"""
dd 
# hello
'www'
"""