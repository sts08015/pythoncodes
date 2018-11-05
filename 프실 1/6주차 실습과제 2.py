from tkinter import *

def processOK():
    name = txt.get()
    print(name+"이(가) 입력됨")

root = Tk()
root.title("GUI 테스트")
lbl = Label(root,text = "이름")
lbl.pack()
txt = Entry(root)
txt.pack()
btn = Button(root,text= "OK", fg = "blue", bg = "gray", command = processOK)
btn.pack()
root.mainloop()
