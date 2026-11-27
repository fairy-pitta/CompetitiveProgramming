"""DFS (深さ優先探索): 始点 s からたどり着ける頂点を調べる。連結成分の個数も数えられる。

    graph = [[1], [0, 2], [1], [4], [3]]   # 0-1-2 と 3-4 の 2 つに分かれている
    dfs(0, 5, graph)        ->  [True, True, True, False, False]
    count_components(5, graph)  ->  2

    # 再帰版 (行きがけ・帰りがけで処理したいとき)
    seen = [False] * 5
    dfs_rec(0, graph, seen)  # seen が [True, True, True, False, False] になる

引数:
    s     : 始点 (0-indexed)
    N     : 頂点数
    graph : 隣接リスト。作り方は build_graph.py の「隣接リスト」
戻り値 (dfs):
    seen[v] = s から v にたどり着けるなら True

使い分け:
    - 最短距離がほしいなら bfs.py (DFS の訪問順は近い順ではない)
    - 連結判定だけならスタック版 dfs か、辺を 1 本ずつ足していくなら unionfind.py
    - 部分木のサイズや帰りがけ順の処理 (木 DP など) が要るなら再帰版 dfs_rec
    - 二部グラフ判定は bipartite.py

仕組み:
    スタック版: スタックから頂点を取り出し、未訪問の隣を訪問済みにして積む。
        deque の popleft を pop に変えただけで BFS と同じ形になる。
    再帰版: v を訪問済みにして、未訪問の隣それぞれについて自分を呼ぶ。
        for の前が「行きがけ」、for の後が「帰りがけ」(子を全部見終わった後) の処理場所。

計算量: O(N + M)。M は辺数。

注意:
    - 再帰版は深さが N になりうるので sys.setrecursionlimit(10**6) が要る。
      PyPy は再帰が遅く、深いとメモリも食うので、帰りがけ処理が要らないならスタック版を使う
    - スタック版は積むときに seen を立てる。取り出すときに立てると同じ頂点を何度も積む
"""
import sys
sys.setrecursionlimit(10 ** 6)

def dfs(s, N, graph):
    seen = [False] * N
    seen[s] = True
    stack = [s]
    while stack:
        v = stack.pop()
        for nv in graph[v]:
            if not seen[nv]:
                seen[nv] = True
                stack.append(nv)
    return seen


def count_components(N, graph):
    # まだ訪問していない頂点から dfs するたびに成分が 1 つ増える
    seen = [False] * N
    cnt = 0
    for s in range(N):
        if seen[s]:
            continue
        cnt += 1
        seen[s] = True
        stack = [s]
        while stack:
            v = stack.pop()
            for nv in graph[v]:
                if not seen[nv]:
                    seen[nv] = True
                    stack.append(nv)
    return cnt


def dfs_rec(v, graph, seen):
    seen[v] = True
    # 行きがけの処理はここ
    for nv in graph[v]:
        if not seen[nv]:
            dfs_rec(nv, graph, seen)
    # 帰りがけの処理はここ
