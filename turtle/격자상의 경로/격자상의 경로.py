import turtle as t
import random as r

x = -80 ; y = 80
t.hideturtle()
t.color("gray")
t.up()
t.goto(x,y)
t.down()
t.speed(100)
for i in range(1,18):
    t.forward(160)
    t.up()
    t.goto(x,y-10*i)
    t.down()

t.up()
t.goto(x,y)
t.down()
t.setheading(270)
for i in range(1,18):
    t.forward(160)
    t.up()
    t.goto(x+10*i,y)
    t.down()

t.width(3)
x = 0;y = 0
t.speed(1)
t.up()
t.goto(0,0)
t.down()
t.showturtle()
t.shape("turtle")
t.color("red")
dx = [10,0,-10,0]
dy = [0,10,0,-10]
while(True):
    k = r.randint(0,3)
    x +=dx[k] ; y+=dy[k]
    if(x > 80 or y > 80 or y < -80 or x < -80):
        break
    t.goto(x,y)
