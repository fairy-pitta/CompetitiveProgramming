# ライブラリさんたち
from collections import deque, Counter, defaultdict
from operator import itemgetter 
from bisect import bisect_right, bisect_left 
from itertools import combinations, permutations, accumulate, product, groupby
import heapq
# from numpy import base_repr
from copy import deepcopy
import sys
# sys.setrecursionlimit(10**6)
from math import gcd, log2, log10
from functools import lru_cache
# @lru_cache(maxsize=None)

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

# 便利な関数くん
def my_lcm(a, b):
    return a * b // gcd(a, b)
def my_ceil(N, W):
    return (-(-N//W))
def out(func):
    if func: print("Yes")
    else: print("No")
import sys
def input(): return sys.stdin.readline()[:-1]
def isint(): return int(input())
def ismap(): return map(int, input().split())
def islist(): return list(input())
def isgraph(N): return [[] for _ in range(N)]
def isdist(N, s): return [(s) for _ in range(N)]
def isseen(N): return [(False) for _ in range(N)]
def iszero(): return list(map(lambda x: int(x) - 1, input().split()))
def sout(list):
    for i in list:
        print(i)

# run-length 
# A = [(k, len(list(g))) for k, g in groupby(map(int, input().split()))]

# 定数ちゃん
# MOD = 998244353
# MOD = 1000000007
# INF = 10 ** 16

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

# v, e, r = ismap()
# graph = isgraph(v)
# for _ in range(e):
#     s, g, c = ismap()
#     graph[s].append((g, c))

# d = dijkstra(r, v, graph)
# print(d)

def main():
    N = isint()
    graph = isgraph(N)
    A = list(ismap())
    B = list(ismap())
    for i in range(N-1):
        if i + 2 <= N - 1:
            graph[i].append((i+2, B[i]))
        graph[i].append((i+1, A[i]))
    
    li = dijkstra(0, N, graph)
    return li[-1]

print(main())





    

