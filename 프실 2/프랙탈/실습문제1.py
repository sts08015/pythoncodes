import turtle as t

def drawTree(x,p):
    if x>=5 and p>=1:
        t.forward(x)
        t.pensize(p-1)
        t.right(30)
        drawTree(x-2.5,p-1)
        t.left(60)
        drawTree(x-2.5,p-1)
        t.right(30)
        t.backward(x)
        
t.pensize(15)
t.color("brown")
t.left(90)
t.forward(100)

t.pensize(15)
t.color("green")
drawTree(25,15)
