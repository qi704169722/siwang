# coding:utf-8
import turtle as t
import time
'''
t.pensize(5)
t.pencolor("yellow")
t.fillcolor("red")

t.begin_fill()

for _ in range(5):
    t.forward(200)
    t.right(144)
t.end_fill()
time.sleep(1)

t.penup()
t.goto(-150, -120)
t.color("violet")
t.write("Done", font=('Consolas', 40, 'normal'))
t.done()

t.color("red", "yellow")
t.speed(10)
t.begin_fill()
for _ in range(50):
    t.forward(200)
    t.left(170)
t.end_fill()
t.done()
'''
def drawSnake(rad, angle, len, neckrad):
    for _ in range(len):
        t.circle(rad, angle)
        t.circle(-rad, angle)
    t.circle(rad, angle/2)
    t.forward(rad/2)  # 直线前进
    t.circle(neckrad, 180)
    t.forward(rad/4)

if __name__ == "__main__":
    t.setup(0.8, 0.8, 0, 0)
    t.penup()
    t.goto(-200,0)
    t.pensize(30)  # 画笔尺寸
    t.pencolor("green")
    t.pendown()
    t.seth(-40)    # 前进的方向
    drawSnake(70, 80, 2, 15)
t.pensize(5)
t.pencolor("yellow")
t.hideturtle()
t.circle(-1)
t.done()
