h,w = map(int,input().split())
M = [[str(x) for x in input().split()] for y in range(h)]

dx = [1,0,-1,0]; dy= [0,1,0,-1]

visit = [[0 for x in range(w)] for y in range(h)]

start = (0,0)
goal = (0,0)


def safe(a,b):
    return (0<=a and a<h) and (0<=b and b<w)

for i in range(h):
    for j in range(w):
        if M[i][j] == 'S':
            start = (i,j)
        elif M[i][j] == 'G':
            goal = (i,j)
            M[i][j] = '.'
#print(goal)

queue = []
queue.append(start)
visit[start[0]][start[1]] = 0

while len(queue)>0:
    cur = queue.pop()
    #print(cur,goal)
    
    if cur[0] == goal[0] and cur[1] == goal[1]:
        #print('ddd')
        break

    for i in range(4):
        a = cur[0] + dx[i]; b = cur[1] + dy[i]
        #print("hee")
        if safe(a,b) and not visit[a][b] and M[a][b] == '.':
            #print(visit[a][b],visit[cur[0]][cur[1]])
            if visit[a][b]!=0:
                visit[a][b] = min(visit[a][b],visit[cur[0]][cur[1]] +1)
            else:
                visit[a][b] = visit[cur[0]][cur[1]] +1
            #print(visit[a][b])
            queue.append((a,b))

#print(M)

#print(visit)

print(visit[goal[0]][goal[1]])
