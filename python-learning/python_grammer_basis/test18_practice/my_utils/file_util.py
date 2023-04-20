def print_file_info(file_name):
    """
    要读取的文件
    :param file_name: 要读取的文件路径
    :return:None
    """
    file = None
    try:
        file = open(file_name, 'r', encoding="UTF-8")
        print(f"{file_name}文件的内容：",file.read())
    except(Exception) as e:
        print(e)
    finally:
        if file: # 如果file是none，则false，否则true
            file.close()
def append_to_file(file_name,data):
    """
    在file_name后追加data
    :param file_name: 要追加内容的文件路径
    :param data: 要追加的内容
    :return: None
    """
    file = open(file_name,'a',encoding="UTF-8")
    file.write(data)
    file.write("\n")
    file.flush()
    file.close()

#  测试一下
if __name__ == '__main__':
    append_to_file("hello.txt", "wwww")
    print_file_info("hello.txt")