# スタートからゴールまでの最短距離を出力する

from collections import deque
# import queue 

# inputs 
Row, Col = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

# minus 1 for 座標の調整
sy -= 1
sx -= 1
gy -= 1
gx -= 1

# 迷路の情報を受け取る
Maze = [input() for _ in range(Row)]

Q = deque()
Q.append([sy, sx])

# 未訪問と始点からの距離を管理する
dist = [[-1] * Col for _ in range(Row)]
dist[sy][sx] = 0

# 移動する4方向
direction = [(0,1), (1,0), (0,-1), (-1, 0)]


while len(Q) > 0:
    y, x = Q.popleft()

    for dy, dx in direction:
        y2 = y + dy
        x2 = x + dx
        
        if not (0 <= y2 <= Row and 0 <= x2 <= Col):
            continue
        if Maze[y2][x2] == "#":
            continue 
        if dist[y2][x2] == -1:
            dist[y2][x2] = dist[y][x] + 1
            Q.append([y2, x2])

print(dist[gy][gx])
