# ナップザック問題　導入編

def solve():
    H, W = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    dp = [[(0) for _ in range(W)] for _ in range(H)]
    field = [[(False) for _ in range(W)] for _ in range(H)]
    field[0][0] = True
    for row in range(H-1):
        for col in range(W):
            if field[row][col]:
                field[row+1][col] = True
                dp[row+1][col] = max(dp[row][col], dp[row+1][col])
                if col + A[row] < W:
                    field[row+1][col+A[row]] = True
                    dp[row+1][col+A[row]] = max(dp[row][col] + B[row], dp[row+1][col+A[row]])
    
    # print(dp)
    if dp[-1][-1] > 0:
        return dp[-1][-1]
    else:
        return -1

print(solve())

