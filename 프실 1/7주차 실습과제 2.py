from tkinter import *
import random as r
colors = ['red','orange','yellow','blue','black','green','pink','purple','brown','gold']

win = Tk()
w = Canvas(win,width=300,height = 200)
w.pack()

for i in range(30):
    idx = r.randint(0,9)
    middle_x = r.randint(0,300)
    middle_y = r.randint(0,200)
    line = r.randint(1,100)
    w.create_rectangle(middle_x - line/2,middle_y - line/2,middle_x + line/2,middle_y + line/2,fill=colors[idx]) 

win.mainloop()
