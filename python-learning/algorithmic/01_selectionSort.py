# 选择排序
# 从小到大
def SelectionSort(a):
    n = len(a)
    for i in range(n - 1):
        min = i  # i为0，1，2，3，4 《=》[0,5)

        for j in range(i + 1, n):  # j为[1,6)
            if a[j] < a[min]:
                min = j
        # 最内侧循环结束，1和8换位置，即a[i]=8,a[min]=1,(i=0,min=2)
        a[i], a[min] = a[min], a[i]
        print(a)


list = [8, 3, 1, 5, 7, 2]
SelectionSort(list)

print("------------")
# 从大到小
def SelectSort_bigToSmall(a):
    n = len(a)
    for i in range(n-1):
        max = i
        for j in range(i+1,n):
            if a[max]<a[j]:
                max = j
        a[i],a[max] = a[max],a[i]
        print(a)
list_big = [3,5,1,7,4,8]
SelectSort_bigToSmall(list_big)