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

from math import factorial
def main():
    N = int(input())
    ans = 1
    k = factorial(N)
    li = factorize(k)
    for i in range(len(li)):
        ans *= (li[i][1]+1) % (10**9+7)

    print(ans % (10**9+7))

main()