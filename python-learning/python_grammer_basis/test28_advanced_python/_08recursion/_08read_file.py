# 递归读取文件
import os

def testos():
    # 列出路径下的内容
    print(os.listdir("./a"))
    # 该路径是否存在
    print(os.path.isdir("./d"))
    # 该路径是不是文件夹
    print(os.path.exists("./a"))

def get_dic_file_list(path):
    """
    :param path:输入的路径
    :return: list，该路径下所有文件的文件列表
    """
    file_list = []
    if os.path.exists(path):
        for x in os.listdir(path):
            new_path = path + "/" + x
            if os.path.isdir(new_path):
                file_list += get_dic_file_list(new_path)
            else:
                file_list.append(new_path)
    else:
        print("该路径不存在，请重新输入")
        return[]
    return file_list

# 测试拼接
def test():
    str = "www"
    a = "qq"
    str += "/"+a
    print(str)

if __name__ == '__main__':
    # testos()
    print(get_dic_file_list("D:/1学习路线/python/递归读文件"))
    # test()