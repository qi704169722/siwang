#coding=utf-8
from random import randint
def RandomArray(n, min, max):
    arr = []
    arr = [randint(min, max) for x in range(n)]
    return arr
alist=RandomArray(9,0,100)
print("原始数列为：",alist)

def bublle(alist):
    n=len(alist)
    flag=False
    for i in range(1,n):
        for j in range(0,n-i):
            if alist[j]>alist[j+1]:
                alist[j],alist[j+1]=alist[j+1],alist[j]
                flag=True
    if not flag:
        return
    return alist

def insert(alist):
    n = len(alist)
    for i in range(1,n):
        key=alist[i]
        pos=i
        while key<alist[pos-1] and pos>0:
            alist[i],alist[i-1]=alist[i-1],alist[i]
            pos-=1
    return alist

def quick(alist,low,high):
    if low>high:
        return
    l=low
    r=high
    key=alist[l]
    while l<r:
        while key < alist[r] and l < r:
            r-=1
        alist[l]=alist[r]
        while key> alist[l] and l < r:
            l+=1
        alist[r] = alist[l]
    alist[l]=key
    quick(alist,low,l-1)
    quick(alist,l+1,high)
    return alist
print("升序排序后：", quick(alist,0,len(alist)-1))


