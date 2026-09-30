N, Q = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

counter = [(0) for _ in range(N)]
seen = set([0])

for _ in range(Q):
    p, x = map(int, input().split())
    counter[p-1] += x

from collections import deque

queue = deque([0])

while queue:
    v = queue.popleft()
    for nv in G[v]:
        if nv in seen:
            continue
        counter[nv] += counter[v]
        seen.add(nv)
        queue.append(nv)

print(*counter)

