# ナップサック問題

def solve():
    # N:ボールの個数
    # M:重さの合計はM以下
    N, M = map(int, input().split())
    # ボールiの重さ
    W = list(map(int, input().split()))
    # ボールiの価値
    V = list(map(int, input().split()))

    dp = [[(-1) for _ in range(M+1)] for _ in range(N+1)]
    dp[0][0] = 0
    m = 0
    # row: 何個ボールを使うか
    # col: 重さは合計いくらになるか
    for row in range(N):
        for col in range(M+1):
            if dp[row][col] == -1:
                continue 
            dp[row+1][col] = max(dp[row][col], dp[row+1][col])
            m = max(m, dp[row+1][col])
            if col + W[row] <= M:
                dp[row+1][col+W[row]] = max(dp[row+1][col+W[row]], dp[row][col] + V[row])
                m = max(m, dp[row+1][col+W[row]])
    return m 

print(solve())

