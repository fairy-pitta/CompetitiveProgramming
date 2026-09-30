N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 10**9+7

slf = 0
oth = 0

for i in range(N):
    for j in range(N):
        if A[i] > A[j]:
            oth += 1
        if i < j and A[i] > A[j]:
            slf += 1

ans = slf * K % MOD

ans += (K-1)*K//2*oth%MOD

print(ans%MOD)