# 部分和問題（応用1）

def main():
    N, M = map(int, input().split())
    W = list(map(int, input().split()))

    dp = [[(10**8) for _ in range(M+1)] for _ in range(N+1)]
    dp[0][0] = 0

    for i in range(N):
        for j in range(M+1):

            dp[i+1][j] = min(dp[i][j], dp[i+1][j])

            if j+W[i] <= M:
                dp[i+1][j+W[i]] = min(
                    dp[i][j+W[i]],
                    dp[i][j]+1,
                    dp[i+1][j+W[i]]
                )
    
    if dp[-1][M] < 10**8:
        print(dp[-1][M])
    else:
        print(-1)

main()