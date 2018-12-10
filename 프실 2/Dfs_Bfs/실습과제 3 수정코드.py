n = int(input())
arr = [[int(i) for i in input().split()] for j in range(n)]
size = [0 for i in range(n)]
cnt = 0
dx = [-1,1,0,0]
dy = [0,0,1,-1]


def safe(i,j):
    if i>=0 and j>=0 and i<n and j<n:
        return True
    else:
        return False

def dfs(a,b,c):
    arr[a][b] = c
    for i in range(4):
        if safe(a+dx[i],b+dy[i]) and arr[a+dx[i]][b+dy[i]] == 1:
            dfs(a+dx[i],b+dy[i],c)
        
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            cnt+=1
            dfs(i,j,cnt+1)

for i in range(n):
    for j in range(n):
        if arr[i][j]:
            size[arr[i][j]-2]+=1

print(cnt)

for i in sorted(size):
    if i is not 0:
        print(i)
