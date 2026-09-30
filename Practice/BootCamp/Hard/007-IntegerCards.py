N, M = map(int, input().split())
A = list(map(int, input().split()))
from sortedcontainers import SortedList
S = SortedList(A)

li = []
for _ in range(M):
    b, c = map(int, input().split())
    li.append((c, b))

li = sorted(li, reverse=True)

for c, b in li:
    for i in range(b):
        v = S.pop(0)
        if v < c:
            S.add(c)
        else:
            S.add(v)
            break

ans = list(S)
print(sum(ans))


