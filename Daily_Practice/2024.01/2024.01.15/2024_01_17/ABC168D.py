import networkx as nx 

N, M = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1 
    G[a].append(b)
    G[b].append(a)

parent = [[-1] for _ in range(N)]
parent[0] = 0

from collections import deque
queue = deque([0])
seen = set([0])

while queue:
    v = queue.popleft()

    for nv in G[v]:
        if nv not in seen:
            parent[nv] = v
            seen.add(nv)
            queue.append(nv)

flag = True
for i in parent:
    if i == -1:
        flag = False

if flag:
    print("Yes")
    for i in parent[1:]:
        print(i+1)
else:
    print("No")


