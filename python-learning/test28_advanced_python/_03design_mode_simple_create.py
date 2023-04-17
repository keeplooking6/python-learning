# 一直都是同一个实例
from _03design_mode_simple_humble import humble

h1 = humble
h2 = humble
print(h1)
print(h2)