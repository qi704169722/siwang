# -*- coding:utf-8 -*-
# ------------------------测试题1----------------------------
# no.2
a={x for x in 'abracadabra' if x not in 'abc'}
print(a)
# 拆开写如下
set_a=set()
for x in 'abracadabra':
    if x not in 'abc':
        set_a.add(x)
print(set_a)
# no.3
dict={'a':1,
      'b':2,
      'c':3
      }
str=list(dict.keys())[list(dict.values()).index(2)]
print(str)
# no.7
print(round(2.615,2))  #四舍五入，第二个参数为精度值
# no.10
list_a=[1,2,3]
list_b=[4,5,6]
for i in zip(list_a,list_b):
    print(i)
# no.12
print('{0:05.2f}'.format(3.14156))     # 0的作用为补齐空格(可不加)，冒号加0则用0补齐.后为精度值，优先度较高
# no.13
f='a{}.txt'
urls=[f.format(page) for page in range(0,3)]
for i in urls:
    print(i)
# no.14
s='  123  '
print(s.strip()) #strip()函数去掉()内的内容
# no.16
str_16='abcdABCD'
print(str_16[0:-1])  #注意此处步进仍然是1
# no.17
list_17='abcdABC'
print(list_17[-2:-3]) #值为空，因为倒序查看但步进却是正向的,固没有符合条件的
# no.19
s1=[1,2,3,'abc',4,5.3]
print(sum(filter(lambda x:isinstance(x,(int)),s1)))
# no.25
print("%05.1f" %3)
print("%05d" %3)  #0作用为补齐0，注意和format函数区别


