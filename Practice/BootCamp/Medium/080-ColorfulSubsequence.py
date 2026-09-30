from collections import defaultdict

def main():
    N = int(input())
    S = input()
    d = defaultdict(int)
    MOD = 10**9+7
    for i in S:
        d[i] += 1

    ans = 1
    for v in d.values():
        ans *= v+1
        ans %= MOD
    
    print((ans-1)%MOD)

main()

    
