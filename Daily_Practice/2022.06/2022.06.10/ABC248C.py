def main():
    N, M, K = map(int, input().split())
    dp = [[0] * (K+1) for _ in range(N+1)]
    dp[0][0] = 1
    MOD = 998244353 

    for ith in range(N):
        for sigma in range(K):
            for k in range(1, M+1):
                if sigma + k > K:
                    break 
                dp[ith+1][sigma+k] += dp[ith][sigma]
                dp[ith+1][sigma+k] %= MOD 
    
    ans = 0 
    for i in range(1, K+1):
        ans += dp[N][i]
        ans %= MOD
    
    return ans 

print(main())




