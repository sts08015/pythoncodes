from tkinter import *  #tkinter module import

def checked(i):  # check button is pressed
    global player
    button = btnarr[i]
    if button['text'] != " ":
        return
    button['text'] = player
    if player == "o":                # changes player
        button['bg'] = "yellow"
        player = "x"
    else :
        player = "o"
        button['bg'] = "lightgreen"

win = Tk()
player = "x"  # player x starts first
btnarr=[]    
for i in range(9):
    btn = Button(win,text=" ",font=("궁서",40),command = lambda k = i: checked(k)) 
    btn.grid(row = i//3,column = i%3) # position of the button
    btnarr.append(btn)  # append pressed button 

win.mainloop()



    
