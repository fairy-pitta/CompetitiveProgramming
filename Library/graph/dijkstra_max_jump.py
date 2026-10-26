"""経路復元つきダイクストラ: 最短距離に加えて「何本の辺を通ったか」と「直前の頂点」も記録する。

    graph = [[(1, 1), (2, 3)], [(2, 1)], []]   # graph[v] = [(行き先, コスト), ...]
    dist = dijkstra(0, 3, graph)
    dist[2]              ->  [2, 2, 1]   # 距離 2、辺 2 本、直前は頂点 1
    get_path(2, dist)    ->  [0, 1, 2]

dijkstra.py との違い:
    dijkstra.py は距離だけを返す。こちらは dist[v] = [距離, 辺の本数, 直前の頂点] を返すので、
    get_path で実際の経路をたどれる。最短距離だけでよいなら dijkstra.py で十分。

最短経路が複数あるときは、その中で辺の本数が最大のものを選ぶ (ファイル名の max jump)。
最小にしたいときは、更新条件の nj > dist[v2][1] を nj < dist[v2][1] に変えるだけでよい。

引数: dijkstra.py と同じ (s は 0-indexed の始点)。
前提: 辺の重みは 1 以上。
    重み 0 の辺があっても最短距離そのものは正しいが、辺数が最大になる保証はなくなる
    (重み 0 の閉路があると辺数はいくらでも増やせるので、そもそも最大が定まらない)。

仕組み:
    更新するときに「どこから来たか (prev)」と辺の本数を一緒に記録しておく。
    v を経由すると (1) 今より短くなる、または (2) 距離は同じで辺の本数が増える、なら上書きする。
    重みが正なら、v2 より距離の小さい頂点はすべて v2 より先にヒープから出てくるので、
    v2 を取り出した時点で v2 への最短経路の候補はすべて比べ終わっている。
    ゴールから prev をたどって始点 (prev = -1) まで戻り、反転すれば始点からの経路になる。

注意: たどり着けない頂点は dist[v][0] が INF のまま。get_path はその頂点 1 つだけを返す。

計算量: O((N + M) log N)。get_path は経路の長さ分。
"""
# dijikstra that computes max jumps
# can recreate the path after distance is clarified


import heapq

def ismap(): return map(int, input().split())
def islist(): return list(input())
def isgraph(N): return [[] for _ in range(N)]
def isdist(N, s): return [(s, 0) for _ in range(N)]
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
        return len(self._container)



INF = 10 ** 18 + 1

def dijkstra(s, N, graph):
    # shorted distance from the start
    # [distance, jumps, prev_v]
    dist = [[INF, 0, -1] for _ in range(N)]
    # start
    dist[s][0] = 0
    seen = isseen(N)
    heap_q = PriorityQueue() # (distance, node)
    heap_q.push((0, s))

    while heap_q:
        _ , v = heap_q.pop()
        # 同じ頂点が何度も積まれることがあるので、2 回目以降は捨てる
        if seen[v]:
            continue
        seen[v] = True
        for adjacent_node in graph[v]:
            v2, cost = adjacent_node[0], adjacent_node[1]
            if seen[v2]:
                continue
            # v を経由したときの距離と辺の本数
            nd = dist[v][0] + cost
            nj = dist[v][1] + 1
            # 短くなる、または同じ距離で辺が増えるなら上書き
            if nd < dist[v2][0] or (nd == dist[v2][0] and nj > dist[v2][1]):
                dist[v2][0] = nd
                dist[v2][1] = nj
                # prev vector
                dist[v2][2] = v
                heap_q.push((nd, v2))

    return dist

def get_path(t, dist):
    """dijkstra の戻り値 dist を使い、始点から t までの頂点列を返す。"""
    path = []
    # 直前の頂点を始点 (-1) までたどる
    while t != -1:
        path.append(t)
        t = dist[t][2]
    # ゴール -> 始点 の順になっているのでひっくり返す
    path.reverse()
    return path
