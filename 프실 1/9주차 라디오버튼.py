from tkinter import * 
from random import *
def display():
    x1=randint(1,200); 
    x2=randint(1,200)
    y1=randint(1,150); 
    y2=randint(1,150)
    color="#%02x%02x%02x" %(randint(1,255),randint(1,255),randint(1,255))
    if v.get()==1:
        cvs.create_line(x1,y1,x2,y2,fill=color)
    elif v.get()==2:
        cvs.create_oval(x1,y1,x2,y2,fill=color)
    elif v.get() == 3:
        cvs.create_rectangle(x1,y1,x2,y2,fill=color)

win = Tk() 
win.title("라디오 버튼")
width = 200
height = 150
cvs = Canvas(win, bg = "white", width = 200, height = 200)
cvs.pack()      
frame1 = Frame(win)
frame1.pack()
v = IntVar()
Radiobutton(frame1, text="선", variable=v, value = 1, command=display).pack(side = LEFT)
Radiobutton(frame1, text="타원", variable=v, value=2, command=display).pack(side = LEFT)
Radiobutton(frame1, text="사각형", variable=v, value=3, command=display).pack(side = LEFT)
win.mainloop()
        
