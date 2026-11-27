"""BFS (幅優先探索): 重みなしグラフで、始点 s から全頂点への最短距離 (辺の本数) を求める。

    graph = [[1, 2], [0, 3], [0], [1]]   # graph[v] = [隣の頂点, ...]
    bfs(0, 4, graph)  ->  [0, 1, 1, 2]   # 0 -> 1 -> 3 で 3 までは 2 本

    grid = ["..#",
            "...",
            "#.."]
    bfs_grid(0, 0, 3, 3, grid)  ->  [[0, 1, -1], [1, 2, 3], [-1, 3, 4]]

引数 (bfs):
    s     : 始点 (0-indexed)
    N     : 頂点数
    graph : 隣接リスト。作り方は build_graph.py の「隣接リスト」
引数 (bfs_grid):
    sy, sx : 始点のマス (行, 列) の順
    H, W   : グリッドの行数・列数
    grid   : 文字列のリスト。"#" が壁
戻り値:
    dist[v] (grid は dist[y][x]) = 始点からの最短距離。たどり着けないところは -1

使い分け:
    - 辺に重みがあるなら dijkstra.py (BFS は全部の辺の長さが 1 のときだけ正しい)
    - 「たどり着けるか」「連結成分」だけなら dfs.py でも BFS でもよい
    - bfs_2d.py は ABC276E 専用の閉路判定。普通のグリッド最短距離はこちらの bfs_grid
    - 多始点にしたいときは、最初に全始点を dist = 0 にして q に積むだけ

仕組み:
    キュー (deque) から近い順に頂点を取り出し、まだ距離が決まっていない (dist == -1) 隣に
    dist + 1 を入れて積む。近い順に取り出されるので、最初に決まった距離が最短になる。
    dist == -1 を訪問済みフラグ代わりに使っているので seen は要らない。

計算量: bfs は O(N + M)、bfs_grid は O(HW)。

注意:
    - list.pop(0) は O(N) で遅い。必ず deque の popleft を使う
    - 積むときに dist を入れる (取り出すときではない)。そうしないと同じ頂点を何度も積む
"""
from collections import deque

def bfs(s, N, graph):
    dist = [-1] * N
    dist[s] = 0
    q = deque([s])
    while q:
        v = q.popleft()
        for nv in graph[v]:
            # まだ距離が決まっていない頂点だけ
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                q.append(nv)
    return dist


def bfs_grid(sy, sx, H, W, grid):
    dist = [[-1] * W for _ in range(H)]
    dist[sy][sx] = 0
    q = deque([(sy, sx)])
    while q:
        y, x = q.popleft()
        # 上・下・左・右
        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny, nx = y + dy, x + dx
            # グリッドの外 / 壁 / 訪問済み はスキップ
            if not (0 <= ny < H and 0 <= nx < W):
                continue
            if grid[ny][nx] == "#" or dist[ny][nx] != -1:
                continue
            dist[ny][nx] = dist[y][x] + 1
            q.append((ny, nx))
    return dist
