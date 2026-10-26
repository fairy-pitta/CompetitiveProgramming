"""経路復元つきダイクストラ: 最短距離に加えて「何本の辺を通ったか」と「直前の頂点」も記録する。

    graph = [[(1, 1), (2, 3)], [(2, 1)], []]   # graph[v] = [(行き先, コスト), ...]
    dist = dijkstra(0, 3, graph)
    dist[2]              ->  [2, 2, 1]   # 距離 2、辺 2 本、直前は頂点 1
    get_path(2, dist)    ->  [0, 1, 2]

dijkstra.py との違い:
    dijkstra.py は距離だけを返す。こちらは dist[v] = [距離, 辺の本数, 直前の頂点] を返すので、
    get_path で実際の経路をたどれる。最短距離だけでよいなら dijkstra.py で十分。

引数・前提: dijkstra.py と同じ (s は 0-indexed の始点、重みは 0 以上)。

仕組み:
    更新するときに「どこから来たか (prev)」を一緒に記録しておく。
    ゴールから prev をたどって始点 (prev = -1) まで戻り、反転すれば始点からの経路になる。
    距離の比較が <= なので、同じ距離の経路が見つかったときも上書きする。

注意:
    - ファイル名は「max jump」だが、同じ距離の経路が複数あるとき「後から見つかった方」で
      上書きするだけで、辺の本数が最大になる保証はない。辺数の最大/最小が問題の条件なら、
      ヒープのキーを (距離, ±辺数) にするなど比較を自分で書き直すこと。
    - たどり着けない頂点は dist[v][0] が INF のまま。get_path はその頂点 1 つだけを返す。

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
    heap_q = PriorityQueue() # (distance, node, jumps)
    heap_q.push((0, s, 0))

    while heap_q:
        # first just needed for heap to sort the nodes
        # nodes (v) is needed to record the vectors
        #
        _ , v, jump = heap_q.pop()
        seen[v] = True
        for adjacent_node in graph[v]:
            v2, cost = adjacent_node[0], adjacent_node[1]
            if not seen[v2] \
                and dist[v][0] + cost <= dist[v2][0]:
                # if all and all
                    # update the cost
                    dist[v2][0] = dist[v][0] + cost
                    # jump
                    dist[v2][1] = jump + 1
                    # prev vector
                    dist[v2][2] = v
                    heap_q.push((dist[v2][0], v2, dist[v2][1]))

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
