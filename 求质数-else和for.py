# 求1-100质数程序
from math import sqrt # 循环嵌套法,注意：else可以和for、while等匹配使用
for n in range(2,101):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            break
    else:
        print(n,end='')
'''
# 函数法
import math 
def su(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
for n in range(2,101):
    if su(n):
        print(n,end=" ")
'''