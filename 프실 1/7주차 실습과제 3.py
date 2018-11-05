import time
from tkinter import *

win = Tk()
c = Canvas(win,width = 400,height = 300)
c.pack()
id = c.create_oval(30,30,50,50,fill="green")

def move_right(event):
    c.move(id,5,0)
def move_left(event):
    c.move(id,-5,0)
def move_up(event):
    c.move(id,0,-5)
def move_down(event):
    c.move(id,0,5)
c.bind_all('<KeyPress-Right>',move_right)
c.bind_all('<KeyPress-Left>',move_left)
c.bind_all('<KeyPress-Up>',move_up)
c.bind_all('<KeyPress-Down>',move_down)
win.mainloop()
