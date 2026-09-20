N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = []
for k in A:
    if k % K == 0:
        ans.append(k//K)

print(*ans)
