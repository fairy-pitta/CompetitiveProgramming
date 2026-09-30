from bisect import bisect_right, bisect_left 
from itertools import accumulate

N, M, P = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
B_accumulated = list(accumulate(B))
B_accumulated.insert(0, 0)
ans = 0


for main in A:
    threshold = P-main
    if threshold <= 0:
        ans += P*M
    else:
        idx = bisect_right(B, threshold)
        ans += B_accumulated[idx] + idx*main + P*(M-idx)

print(ans)