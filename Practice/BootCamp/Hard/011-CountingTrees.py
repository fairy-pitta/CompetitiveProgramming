from collections import defaultdict

N = int(input())
D = list(map(int, input().split()))

d = defaultdict(int)
for i in D:
    d[i] += 1

ans = 1

for v in d.values():
    ans *= v
    ans %= 998244353

if D[0] != 0 or d[0] > 1:
    print(0)
else:
    print(ans)