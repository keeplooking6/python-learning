def add(x,y):
    """

    :param x:第一个加数
    :param y: 第二个加数
    :return: 返回None
    """
    result = x + y
    print(f"{x}+{y}=",result)

add(2,2)

# 能访问x，但不合规矩，正确的是是在外部定义好x，然后访问，num也同样
for x in range(1,4):
    num = "ww"
    print(x,num)
# print(x)
# print(num)

# 局部变量
def say_hello():
    num = 1
    print("hello",num)
say_hello()
money = 5000000
print("请输入您的姓名：",end='')
name = input()
num = None
def menu():
    print("--------------主菜单--------------")
    print("查询余额\t[输入1]")
    print("存款\t[输入2]")
    print("取款\t[输入3]")
    print("退出\t[输入4]")
    print("请输入您的选择：", end='')
    global num
    num = int(input())
def balance():
    print("--------------查询余额--------------")
    print(f"{name},您好，你的余额为：{money}")
def deposit():
    print("--------------存款--------------")
    print("存款成功")
def withdrawal():
    print("--------------取款--------------")
    print("取款成功")
menu()
while(num != 4):
    if(num == 1):
        balance()
        menu()
    elif(num == 2):
        deposit()
        menu()
    elif(num == 3):
        withdrawal()
        menu()
    elif(num == 4):
        print("退出")
        break
    else:
        print("输入不合法，系统已退出")
        break