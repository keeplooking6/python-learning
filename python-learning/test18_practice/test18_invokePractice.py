from my_utils  import file_util
from my_utils  import str_utill
# 字符串倒置
print(str_utill.str_reverse("qwert"))
# 字符串切片
print(str_utill.substr("itheima",1,4))
# 打印某路径下的文件内容
file_util.print_file_info("test18_file.txt")
# 追加内容到某路径下的文件里
file_util.append_to_file("test18_file.txt", "hello")
print("追加后的内容：")
file_util.print_file_info("test18_file.txt")
