# 文件的定义和操作
f = open("1.txt",'r',encoding="UTF-8")
# 一行一行往下读取
print(f.readline())
print(f.readline())
# 读取文件中的前几个字节,不算空格,不指定读取文件全部
print(f.read(11))
print(f.read())
# 读取文件中的所有行,如果上面不注释，就会接着往下读
print(f.readlines())
f.close() # 必须将文件流关闭，否则该文件会一直被python程序占用
# for循环输出文件内容
for line in open("1.txt",'r',encoding="UTF-8"):
    print(line)
    f.close()
with open("1.txt",'r',encoding="UTF-8") as f:
    print(f.readlines())
# practice 统计itheima出现的次数--实现1
file = open("word.txt",'r',encoding="UTF-8")
i = 0
for line in file:
    # str_replace = line.replace("\n","")
    # 或者strip方法
    str_replace = line.strip()
    str_split = str_replace.split(" ")
    for x in str_split:
        if x == "itheima":
            i += 1
print(f"itheima一共出现了{i}次")
file.close()
# 实现2
file = open("word.txt",'r',encoding="UTF-8")
content = file.read()
count = content.count("itheima")
print(f"itheima一共出现了{count}次")
file.close()
# w模式
file = open("2.txt",'w')
file.write("hello")
file.flush()
file = open("2.txt",'a')
# write时还未写入，flush时一次性写入
file.write("\nworld")
file.flush()
# practice
bill_file = open("bill.txt",'r',encoding="UTF-8")
bill_bak = open("bill.txt.bat",'w')
for line in bill_file:
    if(line.__contains__("测试")):
        continue
    print(line)
    bill_bak.write(line)
bill_bak.close()
bill_file.close()

