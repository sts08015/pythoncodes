from tkinter import *
import random as r

root = Tk()
mini = int(input("min : "))
maxi = int(input("max : "))
ans = r.randint(mini,maxi)


lbl0 = Label(root,text = "시작")
lbl0.grid(row=0,column=0)

ent1 = Entry(root)
ent1.grid(row = 1,column = 0,columnspan=3)

def put():
    x = int(ent1.get())
    if x > ans:
        lbl0["text"] = "너무 높아요!!"
    if x < ans:
        lbl0["text"] = "너무 낮아요!!"
    if x == ans:
        lbl0["text"] = "정답!!"
    
def restart():
    ans = r.randint(1,100)
    lbl0["text"] = "시작"
    ent1.delete(0,END)


btn1 = Button(root,text="숫자를 입력",command=put)
btn2 = Button(root,text="게임을 다시 실행",command=restart)

btn1.grid(row=2,column=0)
btn2.grid(row=2,column=1,columnspan=3)

root.mainloop()
