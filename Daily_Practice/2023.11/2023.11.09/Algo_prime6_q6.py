
def factorize(N: int) -> list:
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

def calc_divisors(N) -> list:
    res = []

    for i in range(1, N+1):
        if i * i > N:
            break 

        if N % i != 0:
            continue 

        res.append(i)

        if N // i != i:
            res.append(N // i)
    
    res.sort()

    return res 

import bisect

def main():
    A, B, R, S = map(int, input().split())
    x = A - R
    y = B - S 

    import math 

    gcd = math.gcd(x, y)

    li = calc_divisors(gcd)
    indx = bisect.bisect_right(li, max(x, y))
    if indx == len(li):
        return -1 
    elif indx == 0:
        return li[0]
    else:
        return li[indx-1]





print(main())