## Q1. マス目の経路最適化（１）

def main():
    N = int(input())
    G = [list(map(int, input().split())) for _ in range(3)]

    dp = [[(10**18) for _ in range(N)] for _ in range(3)]
    # 最初の条件
    dp[0][0] = 0
    dp[1][0] = 0
    dp[2][0] = 0

    for grid in range(N-1):
        # (i, grid) から (j, grid+1) への遷移
        for i in range(3):
            for j in range(3):
                cost = abs(G[i][grid]-G[j][grid+1])
                dp[j][grid+1] = min(dp[j][grid+1], dp[i][grid]+cost)
    
    ans = 10**18
    for k in range(3):
        ans = min(ans, dp[k][-1])
    
    print(ans)


main()

