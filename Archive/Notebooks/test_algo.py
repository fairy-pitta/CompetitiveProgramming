def main():
    n = int(input())
    dp = []
    for _ in range(n):
        a = list(map(int, input().split()))
        dp.append(a)
    
    #print(dp)


    for row in range(n):
        for col in range(n):
            if row == 0 and col == 0:
                continue
            elif row == 0 and col-1 >= 0: 
                dp[0][col] += dp[0][col-1]
                #print(dp)
            else:
                if col == 0 and row-1 >= 0:
                    dp[row][0] += dp[row-1][0]
                    #print(dp)
                else:
                    dp[row][col] += max(dp[row-1][col], dp[row][col-1])
                    #print(dp)
    return dp[n-1][n-1]

print(main())
