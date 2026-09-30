def main():
    N = int(input())
    dp = [(0) for _ in range(N)]
    dp[0] = 1

    for i in range(1, len(dp)):
        if i == 1:
            dp[i] += 1
        if i == 2:
            dp[i] += 1
        dp[i] += dp[i-1]
        if i-2 >= 0:
            dp[i] += dp[i-2]
        if i-3 >= 0:
            dp[i] += dp[i-3]

    print(dp[N-1])

main()
