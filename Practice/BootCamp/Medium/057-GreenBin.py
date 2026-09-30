from collections import defaultdict
from operator import mul
from functools import reduce

def cmb(n,r):
    if n <= 1: return 0
    r = min(n-r,r)
    if r == 0: return 1
    nume = reduce(mul, range(n, n - r, -1))
    denom = reduce(mul, range(1, r + 1))
    return nume // denom

def main():
    N = int(input())
    d = defaultdict(int)

    for _ in range(N):
        s = sorted(list(input()))
        s = "".join(s)
        d[s] += 1 
    
    ans = 0
    for v in d.values():
        if v >= 2:
            ans += cmb(v, 2)
    
    print(ans)

main()
    
