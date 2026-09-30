from collections import deque 

H, W = map(int, input().split())
S = []
for _ in range(H):
    s = input()
    S.append(s)

cnt = 0

Seen = [[False] * W for _ in range(H)]

for row in range(H):
    for col in range(W):
        if S[row][col] == "#" and not Seen[row][col]:
            cnt += 1
            d = deque()
            d.append((row, col))
            while d:
                i, j = d.popleft()
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == dc == 0:
                            continue 
                        else:
                            if (0 <= i+ dr < H and
                                0 <= j + dc < W and
                                S[i+dr][j+dc] == "#" and
                                not Seen[i+dr][j+dc]):
                                d.append((i+dr, j+dc))
                                Seen[i+dr][j+dc] = True

print(cnt)




