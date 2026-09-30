n = int(input())
a = sorted(list(map(int, input().split())))

from operator import mul
from functools import reduce

def cmb(n,r):
    if n <= 1: return 0 
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

from bisect import bisect_right, bisect_left 

idx = bisect_right(a, a[-1]//2)
m = a[-1]
pos1 = min(a[idx-1], m-a[idx-1])
pos2 = min(a[idx], m-a[idx])


# res1 = cmb(a[-1], pos1)
# res2 = cmb(a[-1], pos2)

if pos1 >= pos2:
    print(a[-1], a[idx-1])
else:
    print(a[-1], a[idx])

