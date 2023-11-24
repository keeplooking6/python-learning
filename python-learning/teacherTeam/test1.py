# 计算比萨斜塔球落地4次后的总路径长度和第四次弹起后的高度（保留2位小数）

def my_method():
    print("------以下是我的做法------")
    path_sum, height = ball_Length(56, 4)
    print("总路径：", path_sum)
    after = height * 0.25
    print("第四次反弹后的高度：", after)


def ball_Length(height, num):
    i = 0
    sum = 56
    while (i < num - 1):
        height = height * 0.25
        path = height * 2
        i = i + 1
        sum = sum + path
    return sum, height


def answer():
    print("------以下是答案的做法------")
    answer_ball()


def answer_ball():
    s = h = 56
    for i in range(2, 5, 1):
        h = h / 4
        s = s + 2 * h
    print("路径总长度：%.2f,反弹的高度为：%.2f" % (s, h / 4))


if __name__ == '__main__':
    my_method()
    answer()
