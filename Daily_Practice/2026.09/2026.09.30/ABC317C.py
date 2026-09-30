# ABC317C  茶 (diff 604 / 200pt)
# https://atcoder.jp/contests/abc317/tasks/abc317_c




## frequently used functions 
from collections import deque, Counter, defaultdict
from operator import itemgetter 
from bisect import bisect_right, bisect_left 
from itertools import combinations, permutations, accumulate, product, groupby
import heapq
# from numpy import base_repr
from copy import deepcopy
import sys
# sys.setrecursionlimit(10**9)
from math import gcd, log2, log10
from functools import lru_cache, reduce 


def main():
    N, M = map(int, input().split())

    # Nが高々10なので、スタート地点を決めうちすることで
    # 全ての頂点への最大をDFSで求めることができる
    adj = [[] for _ in range(N)]
    for _ in range(M):
        a,b,c = map(int, input().split())
        a -= 1
        b -= 1
        adj[a].append((b, c))
        adj[b].append((a, c))

    maximum = 0

    def dfs(u, visited, cost):
        nonlocal maximum
        maximum = max(maximum, cost)

        for v, w in adj[u]:
            if v not in visited:
                visited.add(v)
                dfs(v, visited, cost + w)
                visited.remove(v)

    for i in range(N):
        visited = {i}
        dfs(i, visited, 0)

    print(maximum)


main()