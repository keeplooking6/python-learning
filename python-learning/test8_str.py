str = "itheima"
print(len(str))
str1 = " itheima and itheima "
# 去掉首尾空格
print(str1.strip())
# 去掉首尾指定字符串
str2 = "12itheima and 12itheima12"
print(str2.strip("12"))
# 取出指定下标的元素
print(str2[4])
print(str2[-2])
# 替换,新建了个字符串，原字符串不变
str3 = str2.replace("12","33")
print(str2)
print(str3)
# 找寻某字符串出现的次数
print(str3.count("it"))
# 找出特定字符串第一次出现的位置
str4 = "itheima and itheima hei"
print(str4.index("hei"))
print(str4.split(" "))
print(str4)
# practice
str5 = "itheima itcast boxuegu"
print(str5.count("it"))
str6 = str5.replace(" ","|")
print(str6)
print(str6.split("|"))

