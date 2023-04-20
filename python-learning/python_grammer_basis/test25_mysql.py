from pymysql import Connection
# 获取mysql的链接对象
conn = Connection(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = 'rootroot',
    autocommit = 'True' # 如果不想手动确认，设置自动提交
)

cursor = conn.cursor()
conn.select_db("learning_mysql")
# 使用游标对象，执行sql语句
# cursor.execute("SELECT * FROM student")
# results: tuple = cursor.fetchall()
# for r in results:
#     print(r)

cursor.execute("INSERT INTO student VALUES(10021,'SS',22,'男')")
# conn.commit() 如果不想手动确认，设置自动提交

# 使用游标对象，执行sql语句
cursor.execute("SELECT * FROM student")
results: tuple = cursor.fetchall()
for r in results:
    print(r)

conn.close()