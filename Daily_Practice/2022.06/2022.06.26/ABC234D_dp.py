def solve():
    H, W = map(int, input().split())
    field = []
    for _ in range(H):
        c = list(input())
        field.append(c)
    dp = [[(0) for _ in range(W)] for _ in range(H)]
    dp[0][0] = 1
    m = 1
    for row in range(H):
        for col in range(W):
            if row == 0 and col == 0:
                continue 
            else:
                if field[row][col] == ".":
                    if row > 0 and dp[row-1][col] > 0:
                        dp[row][col] = max(dp[row-1][col]+1, dp[row][col])
                    if col > 0 and dp[row][col-1] > 0:
                        dp[row][col] = max(dp[row][col-1]+1, dp[row][col])
                    m = max(m, dp[row][col])
    return m 

print(solve())

                