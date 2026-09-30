from collections import defaultdict
from sortedcontainers import SortedList
from copy import deepcopy

N, M, L = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
bad_set = defaultdict(set)

for _ in range(L):
    c, d = map(int, input().split())
    bad_set[c-1].add(d-1)

# print(bad_set)
sub_meal = sorted([(p, j) for j, p in enumerate(B)], reverse = True)
ans = 0
# print(sub_meal)
for i in range(N):
    for p, j in sub_meal:
        if j not in bad_set[i]:
            ans = max(ans, A[i]+p)
            break

print(ans)
