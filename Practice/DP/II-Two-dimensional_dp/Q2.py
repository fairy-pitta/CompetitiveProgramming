
def main():
    N = int(input())
    a = list(map(int, input().split()))
    dp = [[(0) for _ in range(N)] for _ in range(N)]
    dp[0] = a

    for row in range(1, len(dp)):
        for col in range(N):
            dp[row][col] += dp[row-1][col]
            if col-1 >= 0:
                dp[row][col] += dp[row-1][col-1]
            if col + 1 < N:
                dp[row][col] += dp[row-1][col+1]
            dp[row][col] %= 100
    
    print(dp[-1][-1])

main()
            
