from sortedcontainers import SortedList 
from bisect import bisect_right, bisect_left 
Q = int(input())
S = SortedList([])

for i in range(Q):
    li = list(map(int, input().split()))
    if li[0] == 1:
        S.add(li[1])
    elif li[0] == 2:
        idx = S.bisect_right(li[1])
        if idx < li[2]:
            print(-1)
        else:
            print(S[idx-li[2]])
    else:
        idx = S.bisect_left(li[1])
        if idx+li[2] > len(S):
            print(-1)
        else:
            print(S[idx+li[2]-1])