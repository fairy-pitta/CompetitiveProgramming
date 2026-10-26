"""木の直径: 木の上で一番離れた 2 頂点間の距離 (辺の本数)。

使い方 (BFS を 2 回):
    u, _ = diam(1, N, graph)   # 適当な頂点から一番遠い頂点 u を見つける
    v, d = diam(u, N, graph)   # u から一番遠い頂点 v までの距離 d が直径
    # u と v が直径の両端

引数:
    start : BFS の始点
    N     : 頂点数。dist を N+1 個とるので、頂点番号 1〜N の 1-indexed グラフで使える
            (0-indexed でもそのまま動く)
    graph : 重みなしの隣接リスト。graph[v] = [隣の頂点, ...]
戻り値: (start から一番遠い頂点, その距離)

仕組み:
    木では「どこか 1 点から一番遠い頂点」は必ず直径の端の 1 つになる、という性質がある。
    なのでそこからもう一度 BFS して一番遠い頂点までの距離をとれば直径になる。

注意:
    - 変数名は stack だが、popleft しているので中身は BFS のキュー。
    - 辺に重みがある木では使えない (距離の更新を dist[now] + w にした DFS/BFS が必要)。
    - start が孤立点のときは (0, 0) を返す。

計算量: O(N)。
"""
# 木の直径を求める
# 最短経路の最大値

from collections import deque
def diam(start, N, graph):
    # stack を用意、始点を追加
    stack = deque()
    stack.append(start)
    # 始点からの距離を管理
    dist = [(-1) for _ in range(N+1)]
    dist[start] = 0
    # 一番遠い点
    max_point = 0
    # 始点から一番遠い点までの距離
    max_dist = 0
    while len(stack) > 0:
        now = stack.popleft()
        togo = graph[now]
        for point in togo:
            # 訪問済み
            if dist[point] != -1:
                continue
            # これまでで一番遠ければ記録
            elif dist[now] + 1 > max_dist:
                max_point = point

            stack.append(point)
            dist[point] = dist[now] + 1
            max_dist = max(max_dist, dist[now] + 1)

    return max_point, max_dist