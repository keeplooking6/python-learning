# 冒泡排序
# 从小到大
def bubbleSort(a):
    n = len(a)
    # 外层：控制把倒数第一个，倒数第二个。。。丢出比较列表，不再进行比较
    for i in range(n - 1, -1, -1):
        # 内层：第0个和第1个比较，谁大放后面，第1个和第2个比较，谁大放后面，然后将比较完的最大的，放在最后
        for j in range(0,i):
            if a[j] > a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
        print(a)

list = [2, 4, 6, 8, 3]
bubbleSort(list)
