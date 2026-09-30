# ナップサック問題（導入編）

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    dp = [[-1 for _ in range(M)] for _ in range(N)]
    dp[0][0] = 0

    for row in range(N-1):
        for col in range(M):
            if dp[row][col] == -1:
                continue 
            dp[row+1][col] = max(dp[row][col], dp[row+1][col])
            if col+A[row]<M:
                dp[row+1][col+A[row]] = max(dp[row+1][col+A[row]], dp[row][col]+B[row])

    
    print(dp[-1][-1])

main()