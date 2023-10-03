# 定义字典字面量
# {"wxl":100,"ww":22,"gg":44}
# 定义空字典
none_dict = dict()
none_dict2 = {}
# 字典的构造器用法
dict = dict(a=1,b=2,c=3)
print(dict)

my_dict = {"wxl":100,"ww":22,"gg":44}
# 字典的嵌套,字典类型不能作key
my_dict2 = {"ww":my_dict,"www":12}
print(my_dict2["ww"]["gg"])
# 新增元素
my_dict2["wbw"] = 22
print(my_dict2)
# 删除元素
my_dict2.pop("www")
print(my_dict2)
# 更新元素
my_dict2["wbw"] = 222
# 清空字典
my_dict2.clear()
print(my_dict2)
print(len(my_dict))
# 遍历字典
keys = my_dict.keys()
for key in keys:
    print(f"key:{key},value:{my_dict[key]}")
# practice
department = {
    "wlh":{"部门":"科技部门","工资":3000,"级别":1},
    "zjl":{"部门":"科技部门","工资":5000,"级别":2},
    "ljj":{"部门":"科技部门","工资":7000,"级别":3},
    "zxy":{"部门":"科技部门","工资":6000,"级别":1},
}
keys = department.keys()
print("全体员工的信息如下：")
for key in keys:
    print(f"{key}:{department[key]}")
print("全体员工级别为1的进行升级和加薪：")
for key in keys:
    if(department[key]["级别"] == 1):
        department[key]["级别"] = 2
        department[key]["工资"] += 1000
        print(f"{key}:{department[key]}")

