# 1번
n = int(input())

d = int((n-1)/2)

for i in range(-d,d+1):
    for j in range(abs(i)):
          print(" ",end="")
    for j in range(n-2*abs(i)):
        print("*",end="")
    print("")

        
