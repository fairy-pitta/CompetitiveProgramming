# ナップサック問題

def main():
    N, M = map(int, input().split())
    W = list(map(int, input().split()))
    V = list(map(int, input().split()))

    dp = [[(0) for _ in range(M+1)] for _ in range(N+1)]

    for ball in range(N):
        for i in range(M):
            dp[ball+1][i] = max(dp[ball+1][i], dp[ball][i])

            if i+W[ball] <= M:
                dp[ball+1][i+W[ball]] = max(
                    dp[ball][i+W[ball]],
                    dp[ball][i]+V[ball]
                )
    
    print(max(dp[-1]))

main()