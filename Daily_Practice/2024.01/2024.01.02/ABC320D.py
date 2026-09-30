from collections import deque

def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b, x, y = map(int, input().split())
        graph[a].append([b, x, y])
        # 双方向の観測
        graph[b].append([a, -x, -y])

    INF = 10**9+1
    # 各点の座標
    cord = [(INF, INF) for _ in range(N+1)]
    # すでに座標が定まっているかどうか
    seen = [(False) for _ in range(N+1)]
    # 原点よりスタート
    cord[1] = (0, 0)
    seen[1] = True

    def bfs(g):
        que = deque([])
        que.append((1, 0, 0))

        while que:
            v, x, y = que.popleft()
            seen[v] = True
            # 点ｖより観測可能な点の座標を定めます
            for next_v, mx, my in g[v]:
                if seen[next_v]: continue 
                cord[next_v] = (x+mx, y+my)
                que.append((next_v, x+mx, y+my))
    
    bfs(graph)

    for i in range(1, N+1):
        x, y = cord[i]
        if x == y == INF:
            print("undecidable")
        else:
            print(x, y)

main()



