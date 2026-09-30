def main():
    n = int(input())
    dp = []
    for _ in range(n):
        a = list(map(int, input().split()))
        dp.append(a)
    for row in range(n):
        for col in reversed(range(n)):
            if row == 0 and col == n-1:
                continue
            elif row == 0 and col < (n-1):
                dp[0][col] += dp[0][col+1]
            else:
                if col == n-1:
                    dp[row][n-1] += dp[row-1][n-1]
                else:
                    dp[row][col] += min(dp[row-1][col], dp[row][col+1])
    return dp[n-1][0]
print(main())