# Nth fibonacci
def fib(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            print("a:",a,"b:",b)
            a, b = b, a + b
        return b
# 0,1,1,2,3,5
print(fib(5))

# 生成斐波那契数列代码，并且输出斐波那契序列

def fib(n):
    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
        # 输出序列，但不包括前两位
        yield b

for val in fib(6):
    print("val:", val)