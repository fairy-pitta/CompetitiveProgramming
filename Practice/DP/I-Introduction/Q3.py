def main():
    N = int(input())
    dp = [(0) for _ in range(N+1)]
    dp[0] = 1

    for i in range(1, N+1):
        dp[i] += dp[i-1]
        if i-2 >= 0:
            dp[i] += dp[i-2]
    
    print(dp[N])

main()
