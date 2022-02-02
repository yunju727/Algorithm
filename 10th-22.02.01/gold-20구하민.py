from collections import deque

n, m = map(int, input().split())

tomato = [list(map(int, input().split())) for _ in range(m)]
ripen = deque([])
for i in range(m) : 
    for j in range(n) : 
        if tomato[i][j] == 1 : 
            ripen.append((i,j))
            
moves_x = [-1,1,0,0]
moves_y = [0,0,-1,1]
count = 0
while ripen : 
    l = len(ripen)
    for _ in range(l) : 
        x, y = ripen.popleft()
        for i in range(4) : 
            dx = x + moves_x[i]
            dy = y + moves_y[i]
            if dx < 0 or dx >= m or dy < 0 or dy >= n :
                continue
            if tomato[dx][dy] == 0 : 
                tomato[dx][dy] = 1
                ripen.append((dx,dy))
    count += 1

print(-1 if '0' in str(tomato) else count-1)
