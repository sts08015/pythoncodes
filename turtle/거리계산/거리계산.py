import turtle as t
import math as m
t.shape("turtle")
t.color("green")
t.up()
t.goto(-50,34)
t.down()
t.goto(49,-85)
a = ((-50-49)**2 + (34+85)**2)**0.5
t.goto(-0.5,-25.5)
t.write(a)
