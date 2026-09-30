N = int(input())

ng1 = int(input())
ng2 = int(input())
ng3 = int(input())
ng = set([ng1, ng2, ng3])

dp = [(10**18) for _ in range(N+1)]
dp[-1] = 0

for i in reversed(range(1, N+1)):
    if dp[i] < 10**18:
        if i-1 not in ng and i > 0:
            dp[i-1] = min(dp[i-1], dp[i]+1)
        if i-2 not in ng and i > 1:
            dp[i-2] = min(dp[i-2], dp[i]+1)
        if i-3 not in ng and i > 2:
            dp[i-3] = min(dp[i-3], dp[i]+1)

if dp[0] > 100 or N in ng:
    print("NO")
else:
    print("YES")