from tkinter import *

ans = 0
def add():
    global ans
    ans += int(ent1.get())
    lb2["text"] = str(ans)
def sub():
    global ans
    ans -= int(ent1.get())
    lb2["text"] = str(ans)
def reset():
    global ans
    ans = 0
    lb2["text"] = str(ans)
root = Tk()

lb1 = Label(root,text = "현재합계:")
lb2 = Label(root,text = "%d" %ans)
lb1.grid(row=0,column=0)
lb2.grid(row=0,column=1)

ent1 = Entry(root)
ent1.grid(row=1,column=0,columnspan=3)

btn1 = Button(root,text="더하기(+)",command = add)
btn2 = Button(root,text="빼기(-)",command = sub)
btn3 = Button(root,text="초기화",command = reset)

btn1.grid(row=2,column=0)
btn2.grid(row=2,column=1)
btn3.grid(row=2,column=2)

root.mainloop()

