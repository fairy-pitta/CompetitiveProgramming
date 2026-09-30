N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    G[u].append(v)
    G[v].append(u)

def calc(n):
    return (n * (n-1)) // 2

from collections import deque
cnt = 0
color = [(-1) for _ in range(N)]
flag = True

for s in range(N):
    
    if color[s] != -1:
        continue

    color[s] = 0
    black = 0
    white = 0

    queue = deque([s])
    while queue:
        v = queue.popleft()

        if color[v] == 0:
            white += 1
        else:
            black += 1
        
        for nv in G[v]:
            if color[nv] != -1:
                if color[nv] == color[v]:
                    flag = False
                    break 
            else:
                color[nv] = 1-color[v]
                queue.append(nv)
    
    cnt += calc(white) + calc(black) 

ans = calc(N) - M - cnt if flag else 0
print(ans)

int(input())
map(int, input().split())
list(map(int, input().split()))