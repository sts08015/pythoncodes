import turtle as t

def drawTriangle(points):
    t.up()
    t.goto(points[0][0],points[0][1])
    t.down()
    t.goto(points[1][0],points[1][1])
    t.goto(points[2][0],points[2][1])
    t.goto(points[0][0],points[0][1])
    
def getMid(p1,p2):
    x = ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2))
    return x

def sierpinski(points,step):
    drawTriangle(points)
    if step>0:
        for i in range(3):
            if i == 0:
                x = getMid(myPoints[0],myPoints[1])
                t.up()
                t.goto(x[0],x[1])
            elif i == 1:
                x = getMid(myPoints[0],myPoints[2])
                t.up()
                t.goto(x[0],x[1])
            elif i == 2:
                x = getMid(myPoints[1],myPoints[2])
                t.up()
                t.goto(x[0],x[1])

def main():
    t.speed(0)
    myPoints = [[-100,-50],[0,100],[100,-50]]
    n = int(t.textinput("sierpinski triangle","step:"))
    sierpinski(myPoints,n)

main()
