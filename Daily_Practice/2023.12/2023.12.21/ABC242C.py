def main():
    N = int(input())
    dp = [[(0) for _ in range(9)] for _ in range(N)]
    for i in range(9):
        dp[0][i] = 1
    MOD = 998244353
    
    for j in range(N-1):
        for digit in range(9):
            dp[j+1][digit] += dp[j][digit] % MOD
            if digit != 0:
                dp[j+1][digit-1] += dp[j][digit] % MOD
            if digit != 8:
                dp[j+1][digit+1] += dp[j][digit] % MOD

    
    ans = sum(dp[-1]) % MOD
    print(ans)

main()
                