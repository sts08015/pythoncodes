from tkinter import *

def startTimer():
    if(running):
        global timer
        timer +=1
        second = "%02d" %(timer%60)
        minute = "%02d" %((timer//60)%60)
        hour = "%02d" %(timer//3600)
        timeText.configure(text = str(hour) + str(":") + str(minute) + str(":") + str(second))
    window.after(1000,startTimer)
    
def start():
    global running
    running = True

def stop():
    global running
    running = False

running = False
window = Tk()
timer = 0
timeText = Label(window,text = "00:00:00",font = ("새굴림",60,"bold"))
timeText.pack()
startBtn = Button(window,text = "시작",bg ="yellow",command=start)
startBtn.pack(fill=BOTH)
stopBtn = Button(window,text="중지",bg = "yellow",command = stop)
stopBtn.pack(fill=BOTH)
startTimer()
window.mainloop()
