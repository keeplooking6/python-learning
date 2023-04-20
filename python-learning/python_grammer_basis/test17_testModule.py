import test17_mypackage.mymodule1 as m1 # print(1)
import test17_mypackage.mymodule2 as m2 # print(2)
m1.info1()
m2.info2()

from test17_mypackage import mymodule1
from test17_mypackage import mymodule2
mymodule1.info1()
mymodule2.info2()

from test17_mypackage.mymodule1 import info1
from test17_mypackage.mymodule2 import info2
info1()
info2()

from test17_mypackage import *
mymodule1.info1()
# mymodule2.info2() 报错，因为包里的__init__.py的__all__函数只写了mymodule1

