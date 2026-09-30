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
    N, M = inmap()
    graph = [[] for _ in range(N)]
    seen = [(False) for _ in range(N)]
    deg = [(0) for _ in range(N)]
    stack = deque()
    ans = deque()
    for _ in range(M): 
        a, b = inmap()
        graph[b].append(a)
        deg[a] += 1
    for i in range(N):
        graph[i] = sorted(graph[i])
        if deg[i] == 0:
            stack.append(i)
            seen[i] = True 
    while len(stack) > 0:
        v = stack.popleft()
        ans.appendleft(v)
        for v2 in graph[v]:
            if seen[v2]:
                continue 
            deg[v2] -= 1 
            if deg[v2] == 0:
                stack.append(v2)
    print(*list(ans))
main()

    
    
        

