N, W = map(int, input().split())
weights = []
values = []
for _ in range(N):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

dp = [[(-1) for _ in range(W+1)] for _ in range(N+1)]
dp[0][0] = 0

for item in range(1, N+1):
    for val in range(W+1):
        if dp[item-1][val] > -1:
            dp[item][val] = max(dp[item][val], dp[item-1][val])
            if val + weights[item-1] <= W:
                dp[item][val+weights[item-1]] = max(dp[item][val+weights[item-1]], dp[item-1][val]+values[item-1])


print(max(dp[-1]))