from collections import defaultdict
from sortedcontainers import SortedSet

N, Q = map(int, input().split())
A = list(map(int, input().split()))
cnt = defaultdict(int)
mex = SortedSet([])

for i in A:
    cnt[i] += 1

for j in range(N+1):
    if cnt[j] == 0:
        mex.add(j)

for _ in range(Q):
    i, x = map(int, input().split())
    cnt[A[i-1]] -= 1
    cnt[x] += 1
    
    if cnt[A[i-1]] == 0:
        mex.add(A[i-1])
    A[i-1] = x
    if cnt[x] == 1:
        mex.discard(x)
    # print(mex)
    print(mex[0])