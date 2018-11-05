def seat_allocation(arr):
    num = 0
    for i in range(rowCnt):
        for j in range(colCnt):
            if i%2 == 1:
                arr[i][j] = num
                num-=1
            else:
                num+=1
                arr[i][j]  = num
        num+=colCnt
                    
def print_seatTable(arr):
    for i in range(rowCnt):
        for j in range(colCnt):
            print(("%3d" %arr[i][j]),end = "")
        print("")

rowCnt, colCnt=eval(input("행,열의 수:"))
arr = [[0]*colCnt for i in range(rowCnt)]
seat_allocation(arr)
print_seatTable(arr)

