N = int(input())
a = list(map(int, input().split()))
A = sorted(a)
from collections import defaultdict

sa = sum(a)

d = defaultdict(int)

for i in range(N):
    d[A[i]] += 1

d_list = list(d.items())
ans = defaultdict(int)
for i in range(len(d_list)):
    num, t = d_list[i]
    sa = sa-num*t
    ans[num] = sa

print(ans)

for j in range(N):
    print(ans[a[j]])
