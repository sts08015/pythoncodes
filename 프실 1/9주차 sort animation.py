from tkinter import *
import random as r
import time

def doBubble(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
        cvs.delete("block") 
        displayRec(arr)
        time.sleep(0.1)

def doSelection(arr):
    for i in range(len(arr)):
        indexMin = i
        for j in range(i,len(arr)):
            if arr[indexMin] > arr[j]:
                indexMin = j
        arr[i],arr[indexMin] = arr[indexMin],arr[i]
        cvs.delete("block")
        displayRec(arr)
        time.sleep(0.1)

def doInsertion(arr):
    for i in range(1, len(arr)):
        j = i-1
        k = arr[i]
        while arr[j] > k and j >= 0:
            arr[j+1]  = arr[j]
            j -= 1
            arr[j+1] = k
        cvs.delete("block")
        displayRec(arr)
        time.sleep(0.1)
		
        
def displayRec(arr):
    global x,y      
    x=100
    y=380
    for item in arr:
        bar = cvs.create_rectangle(x,y,x+barWidth,y-(item*5),fill="red",tags="block")
        x += barWidth + gap
        cvs.update()        
def displaySort():
    global x,y       
    arr=[]
    for i in range(n):
        arr.append(r.randint(1,50))   
    if v.get() == 1:
        doBubble(arr)   
    elif v.get() == 2:
        doSelection(arr)
    else:
        doInsertion(arr)

width = 940 ; height = 400 ; n=30 ; barWidth = 20 ; gap=5 ; arr=[]
root = Tk()
root.title("정렬 알고리즘 시뮬레이션") 
cvs = Canvas(root, width = width, height = height)
cvs.create_text(500,50, text="Sorting Algorithm", fill="blue",font=('Times',20,"italic"))
cvs.create_text(500,350, text="아래의 라디오 버튼을 클릭하세요", fill="black", tags="block", font=('굴림',10))
cvs.create_rectangle(50,80,900,380)
cvs.pack()
frame1 = Frame(root)
frame1.pack()
v = IntVar()
Radiobutton(frame1, text = "버블정렬",variable=v, value=1, command=displaySort).pack(side = LEFT)
Radiobutton(frame1, text = "선택정렬",variable=v, value=2, command=displaySort).pack(side = LEFT)
Radiobutton(frame1, text = "삽입정렬",variable=v, value=3, command=displaySort).pack(side = LEFT)
root.mainloop()
