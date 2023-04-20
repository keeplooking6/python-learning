list1 = [1,2,3]
dict1 = {"ww":"dd","xx":"1q"}

# 容器类型注解
mylist: list[int] = [1,2,3]
dict1[str,str] = {"ww":"dd","xx":"1q"}

# 联合类型注解
from typing import Union
my_dict: dict[str,Union[int,str]] = {"ww":11,"xx":"1q"}
print(my_dict)

def func(data:Union[int,str]) -> Union[int,str]:
    pass