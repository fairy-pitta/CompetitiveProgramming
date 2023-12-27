from collections import deque

def bfs(y, x, H, W, Graph, sx, sy):
    seen = [[False] * W for _ in range(H)]
    seen[y][x] = True
    queue = deque([(y, x, 1)])

    while queue:
        r, c, dist = queue.popleft()
        next_xy = [(r, c-1), (r, c+1), (r-1, c), (r+1, c)]
        for ny, nx in next_xy:
            if not (0 <= ny < H and 0 <= nx < W):
                continue
            if seen[ny][nx] or ((nx, ny) == (sx, sy) and dist + 1 < 4) or Graph[ny][nx] == "#":
                continue
            if (nx, ny) == (sx, sy):
                return "Yes"
            
            queue.append((ny, nx, dist + 1))
            seen[ny][nx] = True

    return "No"

def main():
    H, W = map(int, input().split())
    C = []
    for i in range(H):
        C.append(input())
        j = C[i].find("S")
        # findは見つからないときは-1を返す
        if j != -1:
            sy, sx = i, j
    
    for y, x in [(sy - 1, sx), (sy + 1, sx), (sy, sx - 1), (sy, sx + 1)]:
        if 0 <= y < H and 0 <= x < W and C[y][x] == ".":
            result = bfs(y, x, H, W, C, sx, sy)
            if result == "Yes":
                return print("Yes")
    
    print("No")

main()
