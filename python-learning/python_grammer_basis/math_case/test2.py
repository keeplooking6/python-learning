
def implement1():
    x = int(input('x = '))
    y = int(input('y = '))
    # 如果x大于y就交换x和y的值
    if x > y:
        # 通过下面的操作将y的值赋给x, 将x的值赋给y
        x, y = y, x
    # 从两个数中较小的数开始做递减的循环
    for factor in range(x, 0, -1):
        print(factor)
        if x % factor == 0 and y % factor == 0:
            print('%d和%d的最大公约数是%d' % (x, y, factor))
            print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
            break

def implement2():
    def gcd(x, y):
        """求最大公约数"""
        (x, y) = (y, x) if x > y else (x, y)
        for factor in range(x, 0, -1):
            if x % factor == 0 and y % factor == 0:
                return factor

    def lcm(x, y):
        """求最小公倍数"""
        return x * y // gcd(x, y)