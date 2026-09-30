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
    A = list(map(int, input().split()))
    d = defaultdict(int)

    for i in A:
        d[i] += 1
    
    cnt = 0
    for v in d.values():
        if v >= 2:
            cnt += cmb(v, 2)
    
    for j in A:
        # print(j, 'j', cnt, d[j])
        ans = cnt
        if d[j] >= 3:
            ans -= cmb(d[j], 2)
            ans += cmb(d[j]-1, 2)
        elif d[j] == 2:
            ans -= 1
        print(ans)

main()


