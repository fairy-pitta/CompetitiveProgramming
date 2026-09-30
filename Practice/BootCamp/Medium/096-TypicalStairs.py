def main():
    N, M = map(int, input().split())
    A = set(int(input()) for _ in range(M))
    MOD = 10**9+7
    dp = [(0) for _ in range(N+1)]
    dp[0] = 1

    for i in range(N):
        if i in A:
            continue
        if i+1 not in A:
            dp[i+1] += dp[i] % MOD
        if i+2 not in A and i+2 < N+1:
            dp[i+2] += dp[i] % MOD
    
    print(dp[-1] % MOD)

main()
