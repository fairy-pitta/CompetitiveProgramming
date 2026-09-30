# [[factor, time]]
def factorize(N) -> list:
    ans = []

    for p in range(2, N):
        # while p * p <= N
        if p * p > N:
            break 

        # if N cannot be divided by p
        # skip p
        if N % p != 0:
            continue 

        # power 
        e = 0
        while N % p == 0:
            e += 1
            N //= p

        ans.append([p, e])
    
    if N != 1:
        ans.append([N, 1])
    
    return ans 

from collections import defaultdict 
from math import gcd 
from functools import reduce

def main():
    N = int(input())
    A = list(map(int, input().split()))
    d = defaultdict(int)

    if reduce(gcd, A) != 1:
        return print("not coprime")
    else:
        for i in A:
            li = factorize(i)
            for fac in range(len(li)):
                d[li[fac][0]] += 1
                if d[li[fac][0]] > 1:
                    return print("setwise coprime")
        
        return print("pairwise coprime")
        


main()

