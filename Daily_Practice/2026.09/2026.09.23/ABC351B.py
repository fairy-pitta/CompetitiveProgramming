# ABC351B  0-100 (diff 0 / 100pt)
# https://atcoder.jp/contests/abc351/tasks/abc351_b




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


from typing import List

# BFSを使って決めうち全探索をしよう！全探索？
def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        A, B = map(int, input().split())
        graph[A].append(B)

    ans = 0
    for start in range(1, N+1):
        seen = [False] * (N+1)
        seen[start] = True
        dq = deque([start])
        ans += 1

        while dq:
            v = dq.popleft()
            for nv in graph[v]:
                if seen[nv]:
                    continue
                seen[nv] = True
                ans += 1
                dq.append(nv)

    print(ans)

    return

main()
