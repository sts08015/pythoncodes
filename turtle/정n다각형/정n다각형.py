import turtle as t
n = int(t.textinput("정다각형","몇각형을 원하시나요?"))
for i in range(n):
    t.forward(100)
    t.right(180-180*(n-2)/n)
    
