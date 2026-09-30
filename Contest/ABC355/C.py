N, T = map(int, input().split())
A = list(map(int, input().split()))

row_cnt = [(0) for _ in range(N)]
col_cnt = [(0) for _ in range(N)]
diag_cnt = [(0), (0)]

ans = -1

for i in range(T):
    number = A[i]

    row_idx = (number-1)//N
    col_idx = (number-1)%N

    row_cnt[row_idx] += 1
    col_cnt[col_idx] += 1 

    if row_idx == col_idx:
        diag_cnt[0] += 1

    if row_idx + col_idx == N-1:
        diag_cnt[1] += 1
    
    if row_cnt[row_idx] == N or col_cnt[col_idx] == N or diag_cnt[0] == N or diag_cnt[1] == N:
        ans = i + 1
        break 

print(ans)