sq_list = [i**2 for i in range(int((10**6)**(0.5))+1)]
sq_set = set(sq_list)

N, M = map(int, input().split())
move_list = []

for j in sq_list:
    if M-j in sq_set:
        x = int(j**(0.5))
        y = int((M-j)**0.5)
        move_list.append((y, x))

G = [set() for _ in range(N*N)]

def add_edges(point: tuple, G : list) -> list:

    cy, cx = point
    poi = cy*N+cx

    for my, mx in move_list:
        if 0 <= (ny := cy-mx) < N and 0 <= (nx := cx-my) < N:
            G[poi].add(ny*N+nx)
        if 0 <= (ny := cy+my) < N and 0 <= (nx := cx-mx) < N:
            G[poi].add(ny*N+nx)
        if 0 <= (ny := cy+mx) < N and 0 <= (nx := cx+my) < N:
            G[poi].add(ny*N+nx)
        if 0 <= (ny := cy-my) < N and 0 <= (nx := cx+mx) < N:
            G[poi].add(ny*N+nx)
    
    return G

# print(add_edges((0, 0), G))
for r in range(N):
    for c in range(N):
        G = add_edges((c, r), G)

from collections import deque

cnt = [(-1) for _ in range(N**2)]
cnt[0] = 0
q = deque([0])

# print(G)

while q:
    cp = q.popleft()

    for np in G[cp]:
        if cnt[np] == -1:
            cnt[np] = cnt[cp]+1
            q.append(np)

ans = [[] for _ in range(N)]

for a in range(len(cnt)):
    ans[a//N].append(cnt[a])

for b in ans:
    print(*b)
    
    




