
def main():
    N = int(input())
    H = list(map(int, input().split()))
    dp = [(-1) for _ in range(N+1)]
    dp[1] = 0
    for jump in range(1, N+1):
        if jump + 1 <= N:
            if dp[jump+1] != -1:
                dp[jump+1] = min(dp[jump+1], dp[jump] + abs(H[jump] - H[jump-1]))
            else:
                dp[jump+1] = dp[jump] + abs(H[jump] - H[jump-1])
        if jump + 2 <= N:
            if dp[jump+2] != -1:
                dp[jump+2] = min(dp[jump+2], dp[jump] + abs(H[jump+1] - H[jump-1]))
            else:
                dp[jump+2] = dp[jump] + abs(H[jump+1] - H[jump-1])
    print(dp)
    return dp[-1]

print(main())
