def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    if N == 1:
        return abs(A[0] - X)
    from math import gcd
    ans = abs(A[0] - X)
    for city in range(N-1):
        gap = abs(A[city] - A[city+1])
        ans = gcd(ans, gap)
    
    return ans

print(main())



