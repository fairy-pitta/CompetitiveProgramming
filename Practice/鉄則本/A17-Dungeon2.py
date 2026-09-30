N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
dp = [([10**18, -1]) for _ in range(N)]

dp[0] = [0, 0]
for i in range(1, N):
    if dp[i][0] > dp[i-1][0] + A[i-1]:
        dp[i][0] = dp[i-1][0] + A[i-1]
        dp[i][1] = i-1
    if i>1 and dp[i][0] > dp[i-2][0] + B[i-2]:
        dp[i][0] = dp[i-2][0] + B[i-2]
        dp[i][1] = i-2


ans = [N]
idx = N-1
while True:
    ans.append(dp[idx][1]+1)
    idx = dp[idx][1]
    if idx == 0:
        break

print(len(ans))
print(*reversed(ans))
