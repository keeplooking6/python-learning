list = [1,2,3,4,5,6,7]
# 从头开始
new_list = list[1:5:]
print(new_list)
new_list = list[::2] #留空代表从头开始，第三个参数代表跳过n-1个元素
print(new_list)

print("----------")

new_list = list[5:2:-1] # 从下标5开始，倒着数到到下标为3的位置，步进为1
print(new_list)
new_list = list[:2:-1] #留空代表从尾开始，倒着数到下标为3的位置，步进为1
print(new_list)
new_list = list[5:1:-2] #从下标为5的地方开始，到下标为2的地方（不含），步进为2，即跳过1个元素倒序输出
print(new_list)
# practice
str = "万过薪月，员序程马黑来，nohtyP学"
# 倒序：str[::-1]，然后切片str[::-1][9:14]，9，14是从末尾开始数的下标(也可以先切片再倒序)
new_str = str[::-1][9:14] #前闭后开
# new_str = str[9:4:-1]

print(new_str)
split_list = str.split("，") # 得到list列表,中英文逗号有区别
print(split_list)
print(split_list[1].replace("来","")[::-1])
