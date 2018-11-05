import turtle as t
import random as r
t.shape("turtle")
t.color("brown")
for i in range(30):
    t.forward(r.randint(1,100))
    t.right(r.randint(0,360))


