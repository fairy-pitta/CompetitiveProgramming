from math import factorial

K = int(input())
C = list(map(int, input().split()))

MOD = 998244353

# DPテーブルの初期化
dp = [[0] * (K + 1) for _ in range(27)]
dp[0][0] = 1

# DPの更新
for i in range(26):
    for j in range(K + 1):
        for k in range(min(C[i], K - j) + 1):
            dp[i + 1][j + k] = (dp[i + 1][j + k] + dp[i][j]) % MOD

# 結果の計算
ans = 0
for i in range(1, K + 1):
    if dp[26][i] > 0:
        unique_permutations = dp[26][i] * factorial(i) % MOD
        ans = (ans + unique_permutations) % MOD

print(ans)
