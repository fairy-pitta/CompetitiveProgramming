N = int(input())
A = list(map(int, input().split()))

from_left = [A[0]]
from_right = [A[-1]]

for i in range(1, N):
    from_left.append(max(from_left[-1], A[i]))
for j in reversed(range(N-1)):
    from_right.append(max(from_right[-1], A[j]))


D = int(input())
for _ in range(D):
    l, r = map(int, input().split())
    l -= 2
    r = (N-1)-r
    print(max(from_left[l], from_right[r]))



