#미완성 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

h,w = map(int,input().split())
arr = [[x for x in input().split()]for y in range(h)]
visit = [[0]*w for i in range(h)]

dx = [0,1,0.-1]
dy = [1,0,-1,0]
ans = 0
pos = (0,0)

for i in range(h):
    for j in range(w):
        if arr[i][j] == 'S':
            pos = (i,j)

queue = []
queue.append(pos)
visit[pos[0]][pos[1]] = 1

for i in range(h):
    for j in range(w):
        if arr[i][j] == 'G':
            pos = (i,j)
            arr[i][j] = '.'

while len(queue)!=0:
    cur = queue.pop()

    if(cur[0] == pos[0] and cur[1] == pos[1]):
        break
    
    for i in range(4):
        if(cur[0]+dx[i]>=0 and cur[0]+dx[i]<w and cur[1]+dy[i]>=0 and cur[1]+dy[i]<h):
            if arr[cur[0]+dx[i]][cur[1]+dy[i]] == '.' :
                queue.append((cur[0]+dx[i],cur[1]+dy[i]))
                visit[cur[0]+dx[i]][cur[1]+dy[i]] = visit[cur[0]][cur[1]] + 1    

print(visit[pos[0]][pos[1]])
