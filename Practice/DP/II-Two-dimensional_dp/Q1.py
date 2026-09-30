
def main():
    a = list(map(int, input().split()))
    dp = [[(0) for _ in range(4)] for _ in range(4)]
    dp[0] = a

    for row in range(1, len(dp)):
        for col in range(4):
            dp[row][col] += dp[row-1][col]
            if col-1 >= 0:
                dp[row][col] += dp[row-1][col-1]
            if col + 1 <= 3:
                dp[row][col] += dp[row-1][col+1]
    
    print(dp[-1][-1])

main()
            
