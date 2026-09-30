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

def bfs(seen, graph, parent, stack):
    while len(stack) > 0:
        now = stack.popleft()
        for v2 in graph[now]:
            if seen[v2]: 
                continue 
            seen[v2] = True 
            parent[v2] = now
            stack.append(v2)
def main():
    N, M, s, t = inmap()
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = inmap()
        graph[a].append(b)
    
    
    stack = deque()
    stack.append(s)
    ans = deque()
    seen = [(False) for _ in range(N)]
    seen[s] = True
    parent = [(-1) for _ in range(N)]

    bfs(seen, graph, parent, stack)
    now = t 
    while now != -1:
        ans.appendleft(now)
        now = parent[now]
    
    print(len(ans))
    print(*list(ans))

main()

