list = [1,2,3,4,5,6,7]
# 从头开始
new_list = list[1:5:]
print(new_list)
new_list = list[::2] #留空代表从头开始，跳过n-1个元素
print(new_list)

print("----------")

new_list = list[5:2:-1]
print(new_list)
new_list = list[:2:-1] #留空代表从尾开始，到下标为2的位置，步进为1
print(new_list)
new_list = list[5:1:-2] #从下标为7的地方开始，到下标为3的地方（不含），步进为2，即跳过1个元素倒序输出
print(new_list)
# practice
str = "万过薪月，员序程马黑来，nohtyP学"
new_str = str[::-1][9:14] #前闭后开
print(new_str)
split_list = str.split("，") # 得到list列表,中英文逗号有区别
print(split_list)
print(split_list[1].replace("来","")[::-1])
