from tkinter import *

def process1():
    temperature = float(ent1.get())
    mytemp = (temperature-32)*5/9
    ent2.delete(0,END)
    ent2.insert(0,str(mytemp))
def process2():
    temperature = float(ent2.get())
    mytemp = 5*temperature/9 + 32
    ent1.delete(0,END)
    ent1.insert(0,str(mytemp))

root = Tk()
root.title("온도변환기")
lbl1 = Label(root,text = "화씨")
lbl2 = Label(root,text = "섭씨")
lbl1.grid(row = 0,column=0)
lbl2.grid(row=1,column=0)
ent1 = Entry(root)
ent2 = Entry(root)
ent1.grid(row=0,column=1)
ent2.grid(row=1,column=1)
btn1 = Button(root,text = "화씨 -> 섭씨",command = process1)
btn2 = Button(root,text = "섭씨 -> 화씨",command = process2)
btn1.grid(row=2,column=0)
btn2.grid(row=2,column=1)
root.mainloop()
