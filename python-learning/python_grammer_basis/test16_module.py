# # 导入模块不同的写法
# import time
# print("开始")
# time.sleep(1)
# print("结束")
#
# from time import sleep
# sleep(1)
#
# from time import *
# sleep(1)
#
# import time as tt
# tt.sleep(1)
#
# from time import sleep as ts
# ts(1)

# 自定义模块
# import test16_DIYmodule1

# 如果自定义模块中运行了其函数，则导入时也会调用该方法,__main__
# import test16_DIYmodule2

# 当导入不同模块相同名称的功能时，下面的会覆盖上面的，所以调用的是下面的方法
# from test16_DIYmodule1 import test_A
# from test16_DIYmodule2 import test_A

# __all__ 可以在import *时控制有哪些功能被导入
# import test16_DIYmodule3 as moudle3
# moudle3.test_A()
# moudle3.test_B()
from test16_DIYmodule3 import *
test_A() # 识别不到test_B()




