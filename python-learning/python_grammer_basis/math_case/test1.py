from math import sqrt

def implement1():
    num = int(input('请输入一个正整数: '))
    # 将输入的数开根号
    end = int(sqrt(num))

    is_prime = True
    # 用输入的正整数除 从2循环到 开根号的每个数 ，如果有取余=0的情况。则说明该正整数不是素数
    for x in range(2, end + 1):
        if num % x == 0:
            is_prime = False
            break
    if is_prime and num != 1:
        print('%d是素数' % num)
    else:
        print('%d不是素数' % num)

def implement2():
    def is_prime(num):
        """判断一个数是不是素数"""
        for factor in range(2, int(num ** 0.5) + 1):
            if num % factor == 0:
                return False
        return True if num != 1 else False