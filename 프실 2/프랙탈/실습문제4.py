import turtle as t

''' [[주의!!!!!!!!!!!!!!!!!!]]
    원 은 중심좌표에서 그리는게 아님 맨 밑에부터 그리는 것임
'''

def getMid(p1,p2):
    x = (p1[0]+p2[0])/2,(p1[1]+p2[1])/2
    return x
    
def draw(r,p):
    t.up()
    print(p[0],p[1])
    t.goto(p[0],p[1])
    t.down()
    t.circle(r)

def yee(points,r,step):

    if step<0 or r<0.01:
        return
    
    draw(r,points[1])
    
    arr = []
    
    arr.append(getMid(points[0],points[1]))
    arr.append(getMid(points[2],points[1]))
    
    yee([points[0],arr[0],points[1]],r/2,step-1)
    yee([points[1],arr[1],points[2]],r/2,step-1)




t.speed(0)
radius = 200

points = [(-radius,-radius),(0,-radius),(radius,-radius)]

t.up()
t.goto(0,-radius)

n = int(t.textinput("creative","step : "))
yee(points,radius,n)
