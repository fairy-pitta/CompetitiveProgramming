

N = int(input())
S = [input() for _ in range(N)]
row_cnt = [S[i].count("o") for i in range(N)]
col_cnt = [(0) for _ in range(N)]

for c in range(N):
    for r in range(N):
        col_cnt[c] += 1 if S[r][c] == "o" else 0

ans = 0


for row in range(N):
    for col in range(N):
        ans += (row_cnt[row]-1) * (col_cnt[col]-1) if S[row][col] == "o" else 0

print(ans)


