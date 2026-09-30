N = int(input())

ng1 = int(input())
ng2 = int(input())
ng3 = int(input())
ng = set([ng1, ng2, ng3])

edges = []

for i in reversed(range(N+1)):
    if i-1 not in ng and i > 0:
        edges.append((i, i-1))
    if i-2 not in ng and i > 1:
        edges.append((i, i-2))
    if i-3 not in ng and i > 2:
        edges.append((i, i-3))

import networkx as nx 

G = nx.DiGraph()
G.add_edges_from(edges)

l = nx.shortest_path_length(G, source=N, target=0)

if l > 100 or N in ng:
    print('NO')
else:
    print("YES")
