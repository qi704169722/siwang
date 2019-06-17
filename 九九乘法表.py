#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# for循环是在序列穷尽时停止，while循环是在条件不成立时停止。
'''
# 打印九九乘法表（正金字塔，=后靠右侧对齐——>使用格式说明符）
for i in range(1,10):
    for j in range(1,10-i):
        print(end="       ")
    for k in range(1,i+1):
        print("%d*%d=%2d" %(i,k,i*k),end=" ")
    print("")
'''
# 打印九九乘法表（正金字塔，=后靠左侧对齐——>使用format函数）
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{}*{}={:<2}".format(j,i,i*j),end=" " if j>1 else "")
#     print()
# format--填充与对齐:^ < > 分别表示居中、左对齐、右对齐，后面为宽度
print('\n'.join([' '.join(['%s*%s=%-2s'%(y,x,x*y)for y in range(1,x+1)]) for x in range(1,10)]))