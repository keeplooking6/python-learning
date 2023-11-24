# 数据的筛选，对比
import numpy as np
import pandas as pd

dates = pd.date_range("20230601",periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])

print(df)
print("---选择某一列---")
print(df.A,df['A'])

print("标签筛选")
print("---第0行到第三行，03-05---")
print(df[0:3],df['20230603':'20230605'])

print("---利用标签选择某一行---")
print(df.loc['20230605'])

print("---利用标签保存所有行的数据，将某几列打印出---")
print(df.loc[:,['A','B']])

print("---利用标签选择某几行数据，将某几列打印出---")
print(df.loc[['20230605','20230602'],['A','B']])

print("索引筛选")
print("---利用索引选择某一行---")
print(df.iloc[3])

print("---利用索引选择3行1列（从0开始）---")
print(df.iloc[3,1])

print("---利用索引选择3行到5行，2列到4列（从0开始）---")
print(df.iloc[3:5,2:4])

print("---利用索引选择某几个行，2列到4列（从0开始）---")
print(df.iloc[[3,4,5],2:4])

print("---综合：第0行到第3行，A,C列---")
# pandas 的 ‘ix’ 属性已经在最新版本中被弃用了。
# print(df.ix[:3,['A','C']])

print("---df---")
print(df)
print("---将A列中大于8的数据筛选出来,对于筛选出来的数据，对其横向行不做要求---")
print(df[df.A>8])

print("---改变某一行的值后，再进行上面的操作---")
df.iloc[4,0] = 2
print(df[df.A>8])

print("---改变值---")
df.iloc[2,1] = 0
print(df)
print("------")
df.loc['20230603','B'] = 1000
print(df)
print("------")

# 改变大于4的所有数字为0
# df[df.A>4]=0
print(df)
print("------")

# 改变A列中大于4的数字为0，但是其所在行不变
df.A[df.A>4]=0
print(df)
print("------")
