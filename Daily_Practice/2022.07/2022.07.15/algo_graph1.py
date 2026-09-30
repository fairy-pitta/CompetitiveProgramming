# ライブラリさんたち
from collections import deque, Counter, defaultdict
from operator import itemgetter 
from bisect import bisect_right, bisect_left 
from itertools import combinations, permutations, accumulate, product
import heapq
# from numpy import base_repr
from copy import deepcopy
import sys
sys.setrecursionlimit(10**6)
from math import gcd, log2, log10

# 便利な関数くん
def my_lcm(a, b):
    return a * b // gcd(a, b)
def my_ceil(N, W):
    return (-(-N//W))
def out(func):
    if func: print("Yes")
    else: print("No")
def inint(): return int(input())
def inmap(): return map(int, input().split())

# 定数ちゃん
# MOD = 998244353
# MOD = 1000000007
# INF = 10 ** 18 + 1

def main():
    N, M, s, t = inmap()
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = inmap()
        graph[a].append(b)
    
    seen = [(False) for _ in range(N)]
    def rec(v):
        seen[v] = True 
        for v2 in graph[v]:
            if seen[v2]:
                continue 
            seen[v2] = True 
            rec(v2)
    
    rec(s)
    return seen[t]

out(main())

