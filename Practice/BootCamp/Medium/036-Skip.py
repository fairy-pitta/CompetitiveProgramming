from math import gcd
from functools import reduce 
from bisect import bisect_right

def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.append(X)
    x = sorted(x)
    gap = []
    ans = 0
    for i in range(1, len(x)):
        gap.append(x[i]-x[i-1])

    ans = reduce(gcd, gap)

    print(ans)

main()