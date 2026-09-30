N = int(input())
A = list(map(int, input().split()))

ans = 0

from collections import defaultdict
from itertools import combinations 

from operator import mul
from functools import reduce

def cmb(n,r):
    if n <= 1: return 0
    r = min(n-r,r)
    if r == 0: return 1
    nume = reduce(mul, range(n, n - r, -1))
    denom = reduce(mul, range(1, r + 1))
    return nume // denom

d = defaultdict(list)
for i in range(N):
    d[A[i]].append(i)

cnt = 0
for key, vlist in d.items():

    if len(vlist) >= 3:
        cnt += cmb(len(vlist), 3)
    
    for li in list(combinations(vlist, 2)):
        f, s = li
        ans += abs(f-s)-1

print(ans-cnt)


