from collections import defaultdict

from operator import mul
from functools import reduce

def cmb(n,r):
    if n <= 1: return 0 
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under


def main():
    N = int(input())
    S = [sorted(input()) for _ in range(N)]

    d = defaultdict(int)
    ans = 0
    for i in S:
        a = "".join(i)
        d[a] += 1 
    
    for k in d.values():
        if k == 1:
            continue 
        ans += cmb(k, 2)

    print(ans)
main()    


