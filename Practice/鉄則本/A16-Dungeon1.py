N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
dp = [(10**18) for _ in range(N)]
dp[0] = 0

for i in range(1, N):
    if i > 1:
        dp[i] = min(dp[i], dp[i-2]+B[i-2])
    dp[i] = min(dp[i], dp[i-1]+A[i-1])

print(dp[-1])
