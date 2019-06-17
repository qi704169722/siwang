# -*- coding:utf-8 -*-


class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class myclass:
    def __init__(self):
        pass

    def zhu(self,num):
        self.num = num
        try:
            k = float(num)
            print(k)
        except MyError as e:
            print(e.msg)

ccc = myclass()
ccc.zhu(input())