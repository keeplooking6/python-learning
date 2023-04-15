import json

from pymysql import Connection
from test24_data_processing import file_define
conn = Connection(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = 'rootroot',
    autocommit = True
)
cursor = conn.cursor()

# 创建数据库，并建表
# cursor.execute("CREATE DATABASE py_sql")
conn.select_db("py_sql")
# cursor.execute("CREATE TABLE orders("
#                "order_date DATE,"
#                "order_id VARCHAR(255),"
#                "money INT,"
#                "province VARCHAR(10));")

text_data = file_define.TextFileReader("../test24_data_processing/2011年1月销售数据.txt")
json_data = file_define.JsonFileReader("../test24_data_processing/2011年2月销售数据JSON.txt")

t_data = text_data.read_file()
j_data = json_data.read_file()

# 插入数据
# for l in t_data:
#     sql = f"INSERT INTO orders VALUES('{l.date}','{l.order_id}',{l.money},'{l.province}')"
#     cursor.execute(sql)
# for l in j_data:
#     sql = f"INSERT INTO orders VALUES('{l.date}','{l.order_id}',{l.money},'{l.province}')"
#     cursor.execute(sql)

cursor.execute("select * from orders")
results: tuple = cursor.fetchall()
f1 = open("fromDatabase.txt",'w',encoding="UTF-8")
for r in results:
    print(r)
    print(r[0])
    data = f"['date':{r[0]},'order_id':{r[1]},'money':{r[2]},'province':{r[3]}]"
    # dict = {"date":r[0],'order_id':r[1],'money':r[2],'province':r[3]}
    f1.write(data)
    break
# f2 = open("fromDatabase.txt",'r',encoding="UTF-8")
# print(f2.readline())


f1.close()
# f2.close()


conn.close()