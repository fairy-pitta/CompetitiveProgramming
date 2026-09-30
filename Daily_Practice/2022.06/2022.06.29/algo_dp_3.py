# 部分和応用１

INF = 10 ** 10
def main():
    N, M = map(int, input().split())
    W = list(map(int, input().split()))
    dp = [[(INF) for _ in range(M+1)] for _ in range(N+1)]
    dp[0][0] = 0
    for row in range(N):
        for col in range(M+1):
            if dp[row][col] == INF:
                continue
            dp[row+1][col] = min(dp[row+1][col], dp[row][col])
            if col + W[row] <= M:
                dp[row+1][col+W[row]] = min(dp[row+1][col+W[row]], dp[row][col] + 1)
    
    # print(dp)
    ans = INF
    for i in range(N+1):
        ans = min(ans, dp[i][M])
    
    if ans < INF:
        return ans 
    else:
        return -1

print(main())