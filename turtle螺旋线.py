from math import sin,cos,pi,sqrt
import turtle as t
t.pensize(2)
t.pencolor(0.2,0.8,0.55) # "#66ccff"
t.speed(10)
'''
# 多彩螺旋线
t.bgcolor("black")
ch=["red","yellow","purple","blue"]
t.tracer(False)
for x in range(400):
    t.forward(2*x)
    t.color(ch[x%4])
    t.left(91)
t.tracer(True)  

'''
# 圆螺旋线
n=50 #number of spirals
d=10 #distance between 2 spirals
r=0  #radius
x,y = 0,0
cur_r = r
for i in range(n):
    for a in range(1,360, 4):
        r = cur_r + d*a/360.0
        a *= pi/180.0
        y = r*sin(a)
        x = r*cos(a)
        t.goto(x,y)
    cur_r += d
'''
# 正螺旋线
for i in range(100):
    t.forward(4*i)
    t.left(90)
t.done()
# 效率找质数
for n in range(2,101):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            break
    else:
        print n,
'''
