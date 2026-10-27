# ABC277E  緑 (diff 1183 / 300pt)
# https://atcoder.jp/contests/abc277/tasks/abc277_e

## frequently used imports
from collections import deque, Counter, defaultdict
from operator import itemgetter
from bisect import bisect_right, bisect_left
from itertools import combinations, permutations, accumulate, product, groupby
from copy import deepcopy
from math import gcd, log2, log10
from functools import lru_cache, reduce
import heapq
import sys
# sys.setrecursionlimit(10**9)


## 入力ヘルパー
# 大量入力のときは input を差し替える
def input(): return sys.stdin.readline().rstrip("\n")
def isint(): return int(input())
def ismap(): return map(int, input().split())
def issmap(): return map(str, input().split())
def islist(): return list(input())
def iszero(): return [int(x) - 1 for x in input().split()]   # 1-indexed を 0-indexed へ


## 出力ヘルパー
def out(cond): print("Yes" if cond else "No")
def sout(xs):
    for x in xs:
        print(x)


## よく使う小道具
def my_lcm(a, b): return a * b // gcd(a, b)
def my_ceil(N, W): return -(-N // W)
def isgraph(N): return [[] for _ in range(N)]
def isdist(N, v): return [v] * N
def isseen(N): return [False] * N

# ランレングス圧縮
# A = [(k, len(list(g))) for k, g in groupby(map(int, input().split()))]


## 定数
# MOD = 998244353
# MOD = 1000000007
INF = 10 ** 18 + 1

class PriorityQueue:
    def __init__(self):
        self._container = []

    def push(self, x):
        heapq.heappush(self._container, x)

    def pop(self):
        return heapq.heappop(self._container)

    def __len__(self):
        return len(self._container)


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


def main():
    N, M, K = ismap()
    graph = isgraph(2 * N)
    for _ in range(M):
        u, v, a = ismap()
        u -= 1
        v -= 1
        # 押される前の頂点と押した後の頂点を区別するために、Nを足して長さ２Nの頂点群にする
        layer = (1 - a) * N
        graph[u + layer].append((v + layer, 1))
        graph[v + layer].append((u + layer, 1))
    for v in iszero():
        off, on = v, v + N  
        graph[off].append((on, 0)) 
        graph[on].append((off, 0))

    dist = dijkstra(0, 2 * N, graph)
    ans = min(dist[N - 1], dist[2 * N - 1])
    print(ans if ans < INF else -1)


main()
