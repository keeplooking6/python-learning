import pandas as pd
import numpy as np

# pd。series列出索引和值
s = pd.Series([1,3,6,np.nan,44,1])
print(s)

dates = pd.date_range('20180606',periods=6)
print(dates)

# 定义随机生成的6行4列的列名称和行索引
# np.random.randn：6行4列的矩阵
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])
print(df)

# 默认的行索引和列名称
df1 = pd.DataFrame(np.arange(12).reshape((3,4)))

# 单独设定每一列的列名称和对应的数据，行索引用默认的
df2 = pd.DataFrame({
    'A':1,
    'B':pd.Timestamp('20130102'),
    'C':pd.Series(1,index=list(range(4)),dtype='float32'),
    'D':np.array([3]*4,dtype='int32'),
    'E':pd.Categorical(["test","train","test","train"]),
    'F':'foo'
})

print(df2)
# 打印出数据的类型
print(df2.dtypes)
# 打印出数据的索引
print(df2.index)
# 打印出数据的列名
print(df2.columns)
print(df2.values)
# describe只能描述一下数字相关，方差，平均值，数量等
print(df2.describe())

print("---df2.T---")
print(df2.T)

print("---df2.sort_index---")
print(df2.sort_index(axis=0,ascending=False))
print(df2.sort_index(axis=1,ascending=False))

print("---sort_values---")
print(df2.sort_values(by='E'))



