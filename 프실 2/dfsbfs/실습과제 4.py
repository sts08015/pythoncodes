h,w = map(int,input().split())
arr = [[x for x in input().split()]for y in range(h)]
visit = [[0]*w for i in range(h)]

dx = [0,1,0.-1]
dy = [1,0,-1,0]
ans = 0
start = (0,0)
end = (0,0)

for i in range(0,h):
    s = arr[i][0]
    for j in range(0,w):
        if s[j] == 'S':
            start = (i,j)
        elif s[j] == 'G':
            end = (i,j)
queue = []
queue.append(start)
visit[start[0]][start[1]] = 0
print(visit)
while len(queue)!=0:
    current = queue[0]
    #print(type(current))
    #print(current[1])
    queue.pop()
    if current[0] == end[0] and current[1] == end[1]:
        break
    for i in range(0,4):
        x = current[0] + dx[i]
        y = current[1] + dy[i]
        #print(i,x,y)
        if x>=0 and x<h and y<w and y>=0:
            if visit[x][y]==0 and arr[x][0][y]=='.':
                visit[x][y] = visit[current[0]][current[1]] +1
                k = (x,y)
                queue.append(k)
                print(visit)

print(visit[end[0]][end[1]])
