import heapq 

def ismap(): return map(int, input().split())
def islist(): return list(input())
def isgraph(N): return [[] for _ in range(N)]
def isdist(N, s): return [(s) for _ in range(N)]
def isseen(N): return [(False) for _ in range(N)]

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
        _ , v = heap_q.pop()
        seen[v] = True 
        for v2, cost in graph[v]:
            if not seen[v2] and dist[v] + cost < dist[v2]:
                dist[v2] = dist[v] + cost 
                heap_q.push((dist[v2], v2))
    
    return dist
