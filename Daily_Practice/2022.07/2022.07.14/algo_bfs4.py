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
    graph = [[] for _ in range(N)]
    deg = [(0) for _ in range(N)]
    for _ in range(M):
        f,s = i_map()
        graph[f].append(s)
        deg[s] += 1

    stack = deque()
    for i in range(N):
        if deg[i] == 0:
            stack.append(i)
    
    while len(stack) > 0:
        t = stack.popleft()
        t_deg = graph[t]
        for task in t_deg:
            deg[task] -= 1 
            if deg[task] == 0:
                stack.append(task)
    
    if sum(deg) == 0:
        return True 
    else:
        return False 

out(main())

