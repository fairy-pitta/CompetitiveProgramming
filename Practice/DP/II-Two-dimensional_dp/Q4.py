def main():
    N = int(input())
    dp = [[(0) for _ in range(N)] for _ in range(N)]
    dp[0][0] = 1

    for row in range(N):
        for col in range(N):
            if col-1 >= 0:
                dp[row][col] += dp[row][col-1]
            if row-1 >= 0:
                dp[row][col] += dp[row-1][col]
    
    print(dp[-1][-1])

main()