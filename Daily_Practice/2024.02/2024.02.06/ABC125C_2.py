N = int(input())
A = list(map(int, input().split()))

from math import gcd 
from collections import deque

left_list = [A[0]]
right_list = deque([A[-1]])

for i in range(N):
    left_list.append(gcd(left_list[-1], A[i]))

for j in reversed(range(N)):
    v = right_list.popleft()
    right_list.appendleft(v)
    right_list.appendleft(gcd(v, A[j]))

left_list = left_list[1:]
right_list = list(right_list)[:-1]


ans = 1
for k in range(N):
    if k == 0:
        ans = max(ans, right_list[k+1])
    elif k == N-1:
        ans = max(ans, left_list[k-1])
    else:
        ans = max(ans, gcd(left_list[k-1], right_list[k+1]))

print(ans)

