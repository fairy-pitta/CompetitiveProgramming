"""ダイクストラ法: 辺の重みが 0 以上のグラフで、始点 s から全頂点への最短距離を求める。

    graph = [[(1, 5), (2, 1)], [], [(1, 2)]]   # graph[v] = [(行き先, コスト), ...]
    dijkstra(0, 3, graph)  ->  [0, 3, 1]        # 0 -> 2 -> 1 の 1 + 2 = 3 が最短

引数:
    s     : 始点 (0-indexed)
    N     : 頂点数
    graph : 隣接リスト。graph[v] に (行き先, コスト) を並べる。作り方は build_graph.py の「重み付き」
戻り値:
    dist[v] = s から v への最短距離。たどり着けない頂点は INF (10^18 + 1) のまま。

使い分け:
    - 重みがすべて 1 (または無し) なら BFS (bfs_2d.py など) の方が速くて簡単
    - 経路の復元や辺数もほしいなら dijkstra_max_jump.py
    - 負の辺があると正しく動かない

仕組み:
    「確定した中で一番近い頂点から順に、その隣の距離を更新する」を繰り返す。
    次に一番近い頂点を毎回 O(log N) で取り出すためにヒープ (優先度付きキュー) を使う。
    ヒープから取り出した頂点 v は距離が確定しているので seen[v] = True にし、
    v の隣 v2 について dist[v] + cost の方が短ければ更新してヒープに積む。

計算量: O((N + M) log N)。M は辺数。
"""
import heapq

def ismap(): return map(int, input().split())
def islist(): return list(input())
def isgraph(N): return [[] for _ in range(N)]
def isdist(N, s): return [(s) for _ in range(N)]
def isseen(N): return [(False) for _ in range(N)]

# heapq を push / pop / len で使えるようにした薄いラッパー (structure/priority_queue.py と同じ)
class PriorityQueue:
    def __init__(self):
        self._container = []

    def push(self, x):
        heapq.heappush(self._container, x)

    def pop(self):
        return heapq.heappop(self._container)

    def __len__(self):
        # これがないと、while pq:が使えません
        return len(self._container)



INF = 10 ** 18 + 1

def dijkstra(s, N, graph):
    # 始点から各頂点への最短距離
    dist = isdist(N, INF)
    # 始点
    dist[s] = 0
    # 訪問済みかどうか
    seen = isseen(N)
    seen[s] = True
    #　仮の距離を記録するヒープ
    heap_q = PriorityQueue() # (distance, node)
    heap_q.push((0, s))

    while heap_q:
        # 距離が一番小さい頂点を取り出す。タプルは 1 要素目 (距離) で比較される
        _ , v = heap_q.pop()
        seen[v] = True
        for v2, cost in graph[v]:
            # 未確定で、v を経由した方が短くなるなら更新
            if not seen[v2] and dist[v] + cost < dist[v2]:
                dist[v2] = dist[v] + cost
                heap_q.push((dist[v2], v2))

    return dist
