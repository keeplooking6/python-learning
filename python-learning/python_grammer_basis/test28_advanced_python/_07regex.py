import re
str = "python and exe,python"

# # match
result = re.match("python",str)
print(result)
# # 找到匹配的字符串下标为？
# print(result.span())
# # 匹配的值为
# print(result.group())

# # search:只找第一个匹配的，后续不再找
# result = re.search("python",str)
# print(result)
# # 找到匹配的字符串下标为？
# print(result.span())
# # 匹配的值为
# print(result.group())

# findall:返回所有匹配的值
# result = re.findall("python",str)
# print(result)

s = "itheima1 @@python2 !!666 "
# 找出全部数字
print(re.findall('\d',s))
# 找出全部的特殊字符
print(re.findall('\W',s))
# 匹配账号，只能由字母和数字组成，长度限制6到10位
regex = "^[0-9a-zA-Z]{6,10}$"
# 匹配QQ号，要求纯数字，长度5-11，第一位不为0
regex2 = "^[1-9][0-9]{5,11}$"
# 匹配邮箱地址，只允许qq、163、gmail这三种邮箱地址
# 邮箱例子：abc.efg.ssh.@qq.com,即{}.{}.{}.{}.{}@{}.{}
regex3 = "^[\w-]+(\.[\w-]+)*@(qq|164|gmail)(\.[\w-]+)+$"
