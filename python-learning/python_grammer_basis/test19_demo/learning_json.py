import json
data = [{"name":"admin","age":18},{"name":"小圆","age":16},{"name":"张三","age":20}]
# 将python数据转为json
data = json.dumps(data,ensure_ascii=False) # 如果不加会导致中文转为json时出现16进制的编码
print(type(data)) # str
print(data)
# 将json转为python数据
data = json.loads(data)
print(type(data))
print(data) # list


