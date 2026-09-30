# 部分和応用２

def out(func):
    if func: print("Yes")
    else: print("No")

def main():
    N, A, B = map(int, input().split())
    X = list(map(int, input().split()))
    dp = [[(False) for _ in range(A+1)] for _ in range(N+1)]
    dp[0][0] = True
    for row in range(N):
        for col in range(A+1):
            if not dp[row][col]:
                continue 
            dp[row+1][col] = True
            dp[row+1][(col + X[row]) % A] = True
    # print(dp)
    return dp[N][B]

out(main())