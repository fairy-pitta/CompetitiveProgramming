# マス目の経路最適化（２）

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    dp = [[(10**18) for _ in range(3)] for _ in range(N)]
    # dp[n][p]
    # p = 0: 上のみ塗る
    # p = 1: 下のみ塗る
    # p = 2: 上下ともに塗る

    # dp[n][0]の最小値は dp[n-1][0]かdp[n-1][2]のどちらかから来る
    # dp[n][1]の最小値は dp[n-1][1]かdp[n-1][2]のどちらかから来る
    # dp[n][2]の最小値は どれから来ても良い

    # 初期条件
    dp[0][0] = A[0]
    dp[0][1] = B[0]
    dp[0][2] = A[0] + B[0]

    for digit in range(1, N):
        dp[digit][0] = min(dp[digit-1][0], dp[digit-1][2]) + A[digit]
        dp[digit][1] = min(dp[digit-1][1], dp[digit-1][2]) + B[digit]
        dp[digit][2] = min(dp[digit-1][0], dp[digit-1][1], dp[digit-1][2]) + A[digit] + B[digit]
    
    ans = min(dp[-1])
    print(ans)

main()




