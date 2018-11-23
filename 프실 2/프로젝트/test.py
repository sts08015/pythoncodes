"""
General Numerical Solver for the 1D Time-Dependent Schrodinger's equation.

author: Jake Vanderplas
email: vanderplas@astro.washington.edu
website: http://jakevdp.github.com
license: BSD
Please feel free to use and modify this, but keep the above information. Thanks!
"""
from tkinter import *
import numpy as np
from matplotlib import pyplot as pl
from matplotlib import animation
from scipy.fftpack import fft,ifft
from method import *

#V0 = 1.2
#a = 1.3
#r = 0.2

def addWall():
    V0 = ent0.get()
    a = ent1.get()
    r = ent2.get()
    bring(V0,a,r)
    
win = Tk()
win.title("프실")
lbl0 = Label(win,text = "U")
lbl1 = Label(win,text = "E/U")
lbl2 = Label(win,text = "L")
lbl3 = Label(win,text = "Add Wall")
lbl4 = Label(win,text = "reset")

ent0 = Entry(win)
ent1 = Entry(win)
ent2 = Entry(win)
ent3 = Entry(win)

#btn0 = Button(win,text = "확인")
btn1= Button(win,text = "Add Wall",command = addWall)
btn2 = Button(win,text = "reset")

lbl0.grid(row=0,column=0)
lbl1.grid(row=1,column=0)
lbl2.grid(row=2,column=0)
lbl3.grid(row=3,column=0)
lbl4.grid(row=4,column=0)

ent0.grid(row=0,column=1)
ent1.grid(row=1,column=1)
ent2.grid(row=2,column=1)
btn1.grid(row=3,column=1)
btn2.grid(row=4,column=1)
