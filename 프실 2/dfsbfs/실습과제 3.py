n = int(input())
arr = [[int(x) for x in input().split()]for y in range(n)]
brr = [[0]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        brr[i][j] = arr[i][j]
        
dx = [0,1,0,-1]
dy = [1,0,-1,0]
ans = 0
tmp = 0
size = [0]*100

def dfs(i,j):
    global tmp
    
    if arr[i][j] == 0: 
        size[ans] = tmp
        return
    else:
        arr[i][j] = 0
        brr[i][j] = ans+1
        tmp+=1
        
    for k in range(4):
        if(i+dx[k]>=0 and i+dx[k]<n and j+dy[k]>=0 and j+dy[k]<n):
            if(arr[i+dx[k]][j+dy[k]]!=0):
                arr[i][j] = 0
                brr[i][j] = ans+1

            dfs(i+dx[k],j+dy[k])


for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            #print(i,j)
            dfs(i,j)
            ans+=1
            tmp = 0
             

for i in range(n):
    for j in range(n):
        print(brr[i][j],end = ' ')
    print()

for i in size:
    if i !=0:
        print(i)
        
print()
print("굴의 수: ", ans)
