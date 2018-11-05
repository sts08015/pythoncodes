from tkinter import *

chk = 0
def signin():
    global chk
    ID = ent1.get()
    PW = ent2.get()
    try:
        file = open("C:\\Users\\sts08\\Desktop\\user.txt","r")
        for line in file:
            line = line.rstrip()
            w_list = line.split(' ')
            if ID in w_list:
                lbl3['text'] = "unavailable id"
                chk = 1

        if chk == 0:
            file.write(ID + ' ' + PW+ '\n')
    except IOError:
        file = open("C:\\Users\\sts08\\Desktop\\user.txt","a")
        lbl3["text"] = "you just made new account!!"
        file.write(ID + ' ' + PW+ '\n')
        
def cancel():
    root.destroy()
    
chk = 0
def login():
    ID = ent1.get()
    PW = ent2.get()
    global chk
    try:
        file = open("C:\\Users\\sts08\\Desktop\\user.txt","r")
        for line in file:
            line = line.rstrip()
            w_list = line.split(' ')
            for i in range(len(w_list)):
                if ID == w_list[0] and PW == w_list[1]:
                    lbl3['text'] = "login complete"
                    chk = 1
            if chk == 0:
                lbl3['text'] = "ID or PW are wrong"
    except IOError:
        lbl3['text'] = "No File"
        
root = Tk()
root.title("로그인")

lbl1 = Label(root,text= "아이디")
lbl2 = Label(root,text = "비밀번호")
lbl3 = Label(root,text = "아이디/비번입력")

lbl1.grid(row = 0,column= 0)
lbl2.grid(row=1,column = 0)
lbl3.grid(row=4,column = 2)

ent1 = Entry(root)
ent1.grid(row=0,column=1,columnspan=3)
ent2 = Entry(root)
ent2.grid(row=1,column=1,columnspan=3)

btn1 = Button(root,text = "로그인",command = login)
btn1.grid(row = 3,column = 2)

btn2 = Button(root,text="취소",command = cancel)
btn2.grid(row=3,column=1)

btn3 = Button(root,text = "회원가입",command = signin)
btn3.grid(row =3,column=3)
