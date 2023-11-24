import numpy as np
# numpy创建二维数组
array = np.array([[1,2,3],
                  [2,3,4]])

print(array)
print('number of dim:',array.ndim) # 几维数组
print('shape:',array.shape) # 几行几列
print('size:',array.size)

# a到b之间生成多少段线段,并指出要生成几行几列的数组
# 1到10之间，分成5段，自动匹配步长
array = np.linspace(1,10,5)
print(array)
# 表示精度，数字越大，精度越高,可以int，可以double，float
array = np.array([[1,2,3],[2,3,4]],dtype=np.int64)
print(array.dtype)

# 生成多少个0，依次列出，并指出要生成几行几列的数组
print("---n行n列的0---")
array = np.zeros(10).reshape((2,5))
print(array)

# 从a到b，依次列出，并指出要生成几行几列的数组
print("---从3到9---")
array = np.arange(3,10)
print(array)

# 3行4列全为1
array = np.ones((3,4))
print(array)

# 3行4列全为空
array = np.empty((5,6))
print(array)

# 减法：
print("---sub---")
a = np.array([10,20,30,40])
b = np.arange(4)

c = a - b
print(c)

# 线性代数运算，元素为矩阵的线性代数运算同下
print("---线性代数---")
a = np.array([10,20,30,40])
b = np.arange(4)
# a和b进行线性运算
c = a.dot(b)
print(c)
c = np.dot(a,b)
print(c)

# 元素维矩阵
a = np.array([[1,1],
              [0,1]])
b = np.arange(4).reshape((2,2))

# 平方运算
print("---square---")
c = np.array((1,2,3,4))
d = c ** 2
print(d)

# sin等三角函数
print("---sin---")
b = 10*np.sin(a) # 对于a的每个sin值
print(b)

# 判断哪些值小于固定值
print("---compare---")
a = np.arange(4)
print(a<3)
print(a==3)

# 随机数，
print("---sum,max,min---")
a = np.random.random((2,4)) # 随机生成的二行四列的数据
print(a)
print(np.sum(a))
print(np.max(a))
print(np.min(a))
print("---行列中找到最大。小的值，1代表行，0代表列---")
print(np.sum(a,axis=1))
print(np.max(a,axis=0))
print(np.min(a,axis=1))

print("------")
a = np.arange(2,14).reshape((3,4))
print(a)
# 平均值
print(np.mean(a))
print(a.mean())
print(np.average(a))
# 也可以算每行里里的平均值
print(np.mean(a,axis=1))
# 累加
print(np.cumsum(a))
# 中位数
print(np.median(a))
# 排序，逐行排序
b = np.arange(14,2,-1).reshape((3,4))
print(b)
print(np.sort(b))
# 最大值索引
print(np.argmax(b))
# 最小值索引
print(np.argmin(b))
# 每个元素之间相差的值
print(np.diff(b))
# 输出非零的数的行列，且结果是行列放在两个数组中
print(np.nonzero(b))
# 矩阵的转置
print(np.transpose(b))
print((b.T).dot(b))
# 在5到9之间的数保持原样，小于5的数变为5，大于9的数写为9
print(np.clip(b,5,9))

print("------")

a = np.arange(1,13).reshape((3,4))
print(a)
print("------")

# 第二行全部输出（数是从0开始）
print(a[2])
# 输出第1行3列
print(a[1][3])
print(a[1,3])
# 输出第一行的全部数
print(a[1,:])
# 输出第一列的全部数
print(a[:,1])
# 输出第2行第1列的数字
print(a[2,1:2])

print(a)
print("------")
# 输出每一行
for row in a:
    print(row)

# 输出每一列
print("------")
for column in a.T:
    print(column)

print("------")
# 将二维数组扁平化
print(a.flatten())
for item in a.flat:
    # 输出每一项
    print(item)

print("------")
print("合并元素")
a = np.array([1,1,1])
b = np.array([2,2,2])

# 列合并
c = np.vstack((a,b))
print(c)
# c:两行三列
print(c.shape)

# 行合并
d = np.hstack((a,b))
print(d)
# d：6行,没有列维度
print(d.shape)

# 加了一个行维度
print(a.shape)
print(a[np.newaxis,:].shape)
# 加了一个列维度
print(a[:,np.newaxis].shape)

# 可以进行多个array合并
print("---多个行合并---")
e = np.concatenate((a,b,b),axis=0)
print(e)
print("---多个行合并---")
# 要给列附上维度意义
a = np.array([1,1,1])[:,np.newaxis]
b = np.array([2,2,2])[:,np.newaxis]
f = np.concatenate((a,b,b),axis=1)
print(f)

# 分割
print("---分割---")
a = np.arange(1,13).reshape((3,4))
print(a)

# 横向分割每一行
print(np.split(a,1,axis=0))
# 纵向分割，两列两列分割，
print(np.split(a,2,axis=1))
# 不均匀分割，分割成3列
print(np.array_split(a,3,axis=1))

# 横向分割，分割成3快
print(np.vsplit(a,3))
# 纵向分割，分割成2快
print(np.hsplit(a,2))

a =  np.arange(1,4)
# 复制，a改变，b也联动改变
b = a
a[2] = 10
print(a)
print(b)
# 复制，a改变，b不改变
print("---------")
b = a.copy()
a[1] = 10
print(a)
print(b)