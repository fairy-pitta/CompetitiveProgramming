# 部分和問題（導入編）

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    dp = [[(False) for _ in range(M)] for _ in range(N)]
    dp[0][0] = True 

    for row in range(1, N):
        for col in range(M):
            dp[row][col] |= dp[row-1][col] 
            if col+A[row-1] < M:
                dp[row][col+A[row-1]] |= dp[row-1][col]
    
    print(sum(dp[-1]))

main()