L, Q = map(int, input().split())

from sortedcontainers import SortedSet
from bisect import bisect_right, bisect_left 

cuts = SortedSet([0, L])

for _ in range(Q):
    c, x = map(int, input().split())
    if c == 1:
        cuts.add(x)
    else:
        left = bisect_right(cuts, x) - 1
        right = bisect_right(cuts, x)
        print(cuts[right] - cuts[left])


