H, W = map(int, input().split())
G = [list(input()) for _ in range(H)]

from collections import deque

dp = [[(10**18) for _ in range(W)] for _ in range(H)]
dp[0][0] = 0 if G[0][0] == "." else 1


for r in range(H):
    for c in range(W):
        for dr, dc in [(1,0), (0, 1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < H and 0 <= nc < W:
                v = 0 if G[nr][nc] == "." else 1
                dp[nr][nc] = min(dp[nr][nc], dp[r][c]+v)

print(dp[-1][-1])