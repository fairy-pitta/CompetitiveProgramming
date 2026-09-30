N, M = map(int, input().split())

from math import ceil
ans = 10**18

for a in range(1, min(int(M**0.5)+2, N+1)):
    b = ceil(M/a)
    if a*b >= M and b <= N:
        ans = min(ans, a*b)

if ans == 10**18:
    print(-1)
else:
    print(ans)
