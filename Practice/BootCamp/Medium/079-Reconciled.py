from math import factorial 

def main():
    N, M = map(int, input().split())
    MOD = 10**9+7

    if abs(N-M) > 1:
        return 0
    
    if N == M:
        return ((factorial(N)%MOD)**2%MOD)*2%MOD
    
    return (factorial(N)%MOD * factorial(M)%MOD)%MOD

print(main())