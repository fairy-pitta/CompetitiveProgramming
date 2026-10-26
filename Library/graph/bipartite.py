"""二部グラフ判定: 頂点を 2 色に塗り分けて、すべての辺の両端を違う色にできるか。

    is_bipartite(3, [[1], [0, 2], [1]])        ->  True   # 0-1-2 の一直線
    is_bipartite(3, [[1, 2], [0, 2], [0, 1]])  ->  False  # 三角形 (奇数長の閉路)

引数:
    N     : 頂点数
    graph : 重みなしの隣接リスト (0-indexed)。無向グラフなら両方向に辺を入れておく
戻り値: 二部グラフなら True

仕組み:
    まだ塗っていない頂点を色 1 で塗り、BFS で隣を反対の色 (1 - 色) で塗っていく。
    隣がすでに同じ色で塗られていたら矛盾なので二部グラフではない。
    連結成分ごとに始点を取り直すので、グラフが連結でなくてもよい。
    「二部グラフ ⇔ 奇数長の閉路がない」とも言える。

計算量: O(N + M)。
"""
# 二部グラフ判定
from collections import deque


def b_judge(now, graph, color, stack):
    """stack に入っている始点から 1 つの連結成分を塗る。矛盾があれば False。

    now は使っておらず (ループ内で上書きされる)、名前は stack だが中身は BFS のキュー。
    """
    while len(stack) > 0:
        now = stack.popleft()
        for v2 in graph[now]:
            # 塗り済みなら色が違うかだけ確認
            if color[v2] != -1:
                if color[v2] == color[now]:
                    return False
                else:
                    continue
            color[v2] = 1 - color[now]
            stack.append(v2)

    return True


def is_bipartite(N, graph) -> bool:
    """連結でないグラフも含めて二部グラフか判定する"""
    # -1: 未塗装, 0 / 1: 色
    color = [-1] * N
    for start in range(N):
        if color[start] != -1:
            continue
        color[start] = 1
        stack = deque([start])
        if not b_judge(start, graph, color, stack):
            return False
    return True
