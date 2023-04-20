def str_reverse(s):
    """
    将字符串倒置
    :param s: 用户输入的字符串
    :return: 返回倒置后的字符串
    """
    s_reverse = s[::-1]
    return s_reverse
# 对字符串进行切片，从x到y
def substr(s,x,y):
    """
    将字符串从x到y进行切片
    :param s: 用户输入的字符串
    :param x: 切片开始的下标
    :param y: 切片结束的下标
    :return: 返回切片后的字符串
    """
    return s[x:y]
