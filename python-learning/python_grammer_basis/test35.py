def get_suffix(filename, has_dot=False):
    """
    获取文件名的后缀名

    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
    """
    pos = filename.rfind('.')
    print(pos)
    if 0 < pos < len(filename) - 1:
        # has_dot为True，代表需要带点，就从点的位置开始切片
        # has_dot为False，代表不需要带点，就从点的后一个位置开始切片
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''
print(get_suffix("hello.txt",has_dot=True))