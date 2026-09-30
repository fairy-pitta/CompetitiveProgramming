from operator import mul
from functools import reduce

def cmb(n,r):
    if n <= 1: return 0
    r = min(n-r,r)
    if r == 0: return 1
    nume = reduce(mul, range(n, n - r, -1))
    denom = reduce(mul, range(1, r + 1))
    return nume // denom