from sortedcontainers import SortedList
from bisect import bisect_right, bisect_left

N = int(input())

events = SortedList([])
index = 1
for i in range(N):
    l, r = map(int, input().split())
    index += 2
    events.add((l, 'start', r, i))
    events.add((r, 'end', l, i))

intersection_count = 0
S = SortedList() 
len_S = 0

for point, kind, other_end, idx in events:
    if kind == "start":
        pos = S.bisect_left(point)
        # print(S, pos, len(S), len_S, (point, kind, other_end))
        intersection_count += len_S - pos
        S.add(other_end)
        len_S += 1
    else:
        S.discard(other_end)  


print(intersection_count)
