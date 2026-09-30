# 部分和問題

def main():
    N, M = map(int, input().split())
    W = list(map(int, input().split()))

    dp = [[(False) for _ in range(M+1)] for _ in range(N+1)]
    dp[0][0] = True 

    for ball in range(1, N+1):
        for weight in range(M+1):
            dp[ball][weight] |= dp[ball-1][weight]
            if weight + W[ball-1] <= M:
                dp[ball][weight+W[ball-1]] |= dp[ball-1][weight]
    
    # print(dp)

    if dp[-1][M]:
        print("Yes")
    else:
        print("No")

main()
