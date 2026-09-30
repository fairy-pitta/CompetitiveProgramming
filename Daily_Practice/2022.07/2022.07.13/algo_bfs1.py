# ライブラリさんたち
from collections import deque, Counter, defaultdict
from operator import itemgetter 
from bisect import bisect_right, bisect_left 
from itertools import combinations, permutations, accumulate, product
import heapq
# from numpy import base_repr
from copy import deepcopy
import sys
# sys.setrecursionlimit(10**6)
from math import gcd, log2, log10

# 便利な関数くん
def my_lcm(a, b):
    return a * b // gcd(a, b)
def my_ceil(N, W):
    return (-(-N//W))
def printout(func):
    if func: print("Yes")
    else: print("No")
def i_int(): return int(input())
def i_map(): return map(int, input().split())

# 定数ちゃん
# MOD = 998244353
# MOD = 1000000007
# INF = 10 ** 18 + 1


def main():
    N, M = i_map()
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = i_map()
        graph[a].append(b)
        graph[b].append(a)
    
    visiting = [[] for _ in range(N+1)]
    seen = [(False) for _ in range(N+1)]

    for k in range(N):
        if k == 0:
            visiting[0].append(k)
            seen[0] = True
            print(*visiting[k])
        else:
            for pv in visiting[k-1]:
                togo = graph[pv]
                for v in togo:
                    if seen[v]:
                        continue 
                    seen[v] = True
                    visiting[k].append(v)
            visiting[k] = sorted(visiting[k])
            print(*visiting[k])

main()




