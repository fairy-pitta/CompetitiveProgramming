N = int(input())
A = sorted(list(map(int, input().split())))
MOD = 998244353
ans = 0

for i in range(N):
    ans += A[i]**2 % MOD

