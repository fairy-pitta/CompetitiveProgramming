N, M = map(int, input().split())

from sortedcontainers import SortedList
A = SortedList(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

ans = 0

for i in range(M):
    cost = B[i]
    idx = A.bisect_left(cost)
    if idx != len(A):
        ans += A[idx]
        A.discard(A[idx])
        # print(A)
        # print(ans)
    else:
        ans = -1
        break

print(ans)
