# -*- coding:utf-8 -*-
# 斐波那契数列第n项
import time
def f1(n):
    a=int(1)
    b=int(1)
    for i in range (n-2):
        a,b=b,a+b
    return b
t=time.time()
print("请输入数字")
n=int(input())
print(str(f1(n)))
print(time.time()-t)
