def calc(n):
    return (n+1)*n//2

from bisect import bisect_right, bisect_left 

N, K = map(int, input().split())
A = list(map(int, input().split()))

B = [0]
for i in A:
    B.append(B[-1]+i)

ans = 0

for i in range(len(B)):
    cutoff = B[i] + K
    idx = bisect_left(B, cutoff)
    ans += len(B)-idx

print(ans)
