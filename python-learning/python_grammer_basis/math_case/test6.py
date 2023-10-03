def fib(n):
    a, b = 0, 1
    for _ in range(n):
        # 类似x,y = y,x一样
        a, b = b, a + b
        # yield 算一次返回一次【生成器】
        yield a


def main():
    for val in fib(20):
        print("val:",val)


if __name__ == '__main__':
    main()

