# 2、设计一个抽象类，确定有哪些功能（定义文件读取的相关功能），并使用子类实现相关功能
import json

from data_define import Record
class Reader:
    def read_file(self) -> list[Record]:
        """读取文件的数据，读取到的每一条转换成Record数据类型，并封装到list列表中"""
        pass

# 文件读取
class TextFileReader(Reader):
    # 文件读取时，输入路径
    def __init__(self,path):
        self.path = path

    # 文件具体读取实现方法
    def read_file(self) -> list[Record] :
        record_list: list[Record] = []

        f = open(self.path,'r',encoding="UTF=8")
        for line in f.readlines():
            line = line.strip() # 消除每一行的回车
            data_list = line.split(",") # 得到一行中每一块的数据
            record = Record(data_list[0],data_list[1],data_list[2],data_list[3])
            record_list.append(record)

        f.close()
        return record_list

# Json文件读取
class JsonFileReader(Reader):
    # 文件读取时，输入路径
    def __init__(self,path):
        self.path = path

    # 文件具体读取实现方法
    def read_file(self) -> list[Record] :
        record_list: list[Record] = []

        f = open(self.path,'r',encoding="UTF=8")
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict["date"],data_dict["order_id"],data_dict["date"],data_dict["date"])
            record_list.append(record)

        f.close()
        return record_list

if __name__ == '__main__':
    text_read = TextFileReader("2011年1月销售数据.txt")
    list1 = text_read.read_file()
    for l in list1:
        print(str(l))

    # json_read = JsonFileReader("2011年2月销售数据JSON.txt")
    # list2 = json_read.read_file()
    # for l in list2:
    #     print(str(l))