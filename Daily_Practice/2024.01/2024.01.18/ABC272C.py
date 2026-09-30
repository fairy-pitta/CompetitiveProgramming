
sq_list = [i**2 for i in range(int((10**6)**(0.5))+1)]
sq_set = set(sq_list)

N, M = map(int, input().split())
move_list = []

for j in sq_list:
    if M-j in sq_set:
        x = int(j**(0.5))
        y = int((M-j)**0.5)
        move_list.append((y, x))

grid = [[(-1) for _ in range(N)] for _ in range(N)]
grid[0][0] = 0

from collections import deque

q = deque([(0, 0)])
cnt = 0

while q:
    cy, cx = q.popleft()
    
    if cnt > 10**6:
        break

    for mx, my in move_list:

        # top 
        if 0 <= (nx := cx+my) <N and 0 <= (ny := cy-mx) < N:
            grid[ny][nx] = grid[cy][cx] + 1 if grid[ny][nx] == -1 else min(grid[ny][nx], grid[cy][cx]+1)
            q.append((ny, nx))
        if 0 <= (nx := cx-my) < N and 0 <= (ny := cy-mx) < N:
            grid[ny][nx] = grid[cy][cx] + 1 if grid[ny][nx] == -1 else min(grid[ny][nx], grid[cy][cx]+1)
            q.append((ny, nx))
        
        # right
        if 0 <= (nx := cx+mx) < N and 0 <= (ny := cy-my) < N:
            grid[ny][nx] = grid[cy][cx] + 1 if grid[ny][nx] == -1 else min(grid[ny][nx], grid[cy][cx]+1)
            q.append((ny, nx))
        if 0 <= (nx := cx+mx) < N and 0 <= (ny := cy+my) < N:
            grid[ny][nx] = grid[cy][cx] + 1 if grid[ny][nx] == -1 else min(grid[ny][nx], grid[cy][cx]+1)
            q.append((ny, nx))
        
        # down
        if 0 <= (nx := cx+my) < N and 0 <= (ny := cy+mx) < N:
            grid[ny][nx] = grid[cy][cx] + 1 if grid[ny][nx] == -1 else min(grid[ny][nx], grid[cy][cx]+1)
            q.append((ny, nx))
        if 0 <= (nx := cx-my) < N and 0 <= (ny := cy+mx) < N:
            grid[ny][nx] = grid[cy][cx] + 1 if grid[ny][nx] == -1 else min(grid[ny][nx], grid[cy][cx]+1)
            q.append((ny, nx))
        
        # left 
        if 0 <= (nx := cx-mx) < N and 0 <= (ny := cy-my) < N:
            grid[ny][nx] = grid[cy][cx] + 1 if grid[ny][nx] == -1 else min(grid[ny][nx], grid[cy][cx]+1)
            q.append((ny, nx))
        if 0 <= (nx := cx-mx) < N and 0 <= (ny := cy+my) < N:
            grid[ny][nx] = grid[cy][cx] + 1 if grid[ny][nx] == -1 else min(grid[ny][nx], grid[cy][cx]+1)
            q.append((ny, nx))
        
        cnt += 1

flag = True

for r in range(N):
    if -1 in grid[r]:
        flag = False

if flag:
    for row in grid:
        print(*row)
else:
    print(-1)

        
        
    