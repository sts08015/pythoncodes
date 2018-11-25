import turtle as t

def drawTriangle(points):
    t.up()
    t.goto(points[0][0],points[0][1])
    t.down()
    for i in range(1,len(points)):
        t.goto(points[i][0],points[i][1])
    t.goto(points[0][0],points[0][1])
    
def getMid(p1,p2):
    x = (p1[0]+p2[0])/2,(p1[1]+p2[1])/2
    return x

def sierpinski(points,step):
    drawTriangle(points)
    arr = []
    if step>0:
        #print(3)
        for i in range(3):
            #print(i)
            for j in range(i+1,3):
                x = getMid(points[i],points[j])
                arr.append(x)

        sierpinski([points[0],arr[0],arr[1]],step-1)
        sierpinski([points[1],arr[0],arr[2]],step-1)
        sierpinski([points[2],arr[1],arr[2]],step-1)
                    
                
                
def main():
    t.speed(0)
    myPoints = [[-100,-50],[0,100],[100,-50]]
    n = int(t.textinput("sierpinski triangle","step:"))
    sierpinski(myPoints,n)

main()
