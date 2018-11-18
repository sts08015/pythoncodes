import turtle as t

def draw(length,chk):
    t.color(a[chk%5])
    if length<=1:
        return
    
    t.right(45)
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length/2)
    draw(length/(2**0.5),chk+1)
    

a = ["green","red","blue","purple","black"]
t.up()
t.goto(-250,250)
t.down()
t.pensize(3)
t.left(45)
draw(500,0)
