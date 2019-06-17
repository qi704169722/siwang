# -*- coding:utf-8 -*-
# 拆包
dict_01={"a":1,"b":2,"c":3}
for key,value in dict_01.items():
    print(key,value)

list= ["aa","bb","cc"]
values = [0.1,0.2,0.3]
for x,y in zip(list,values):
    print(x,y)

def outer():
    num=10
    def inner():
        nonlocal num
        num=100
        print(num)
    inner()
    print(num)
outer()

class dog():
    color='red'
    tail=True
    def introduce(self,color):
        self.color=color
        print(self.color)
wang=dog()
wang.introduce('yellow')
print(wang.tail)

class Dog():
    def __init__(self,color,tail):
        self.color = color
        self.tail = tail
wangcai = Dog(" 毛色：yellow", " 长尾巴",)
erha = Dog(" 毛色：black", " 短尾巴",)
print(wangcai.color,wangcai.tail)
print(erha.color,erha.tail)

class Test(object):
    ID = 1
    def __init__(self):
        pass
    def prtID(self):
        print(self.ID)
    def classplusOne(self):
        Test.ID += 1
    def ObjplusOne(self):
        self.ID += 1
t1 = Test()
t2 = Test()
print(t1.classplusOne())

print('=hello'.join('abc'))


