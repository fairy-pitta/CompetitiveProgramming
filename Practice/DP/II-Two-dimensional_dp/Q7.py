def main():
    N = int(input())
    S = []
    for _ in range(N):
        S.append(list(map(int, input().split()))[::-1])
    dp = [[(10**18) for _ in range(N)] for _ in range(N)]
    dp[0][0] = S[0][0]

    for row in range(N):
        for col in range(N):
            if col-1 >= 0:
                dp[row][col] = min(dp[row][col], dp[row][col-1] + S[row][col])
            if row-1 >= 0:
                dp[row][col] = min(dp[row][col], dp[row-1][col] + S[row][col])
    
    print(dp[-1][-1])

main()