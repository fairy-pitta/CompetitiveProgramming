def main():
    n,m = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [[False] * m for _ in range(n)]

    dp[0][0] = True
    for row in range(n-1):
        for col in range(m):
            if dp[row][col] == True: 
                dp[row+1][col] = True
                if A[col] + col <= m-1:
                    dp[row+1][col + A[col]] = True
            print(dp)
    return sum(dp[n-1])

print(main())



