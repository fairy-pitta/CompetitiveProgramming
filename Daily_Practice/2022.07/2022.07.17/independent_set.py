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
def out(func):
    if func: print("Yes")
    else: print("No")
def inint(): return int(input())
def inmap(): return map(int, input().split())
def inlist(): return list(input())
def ingraph(N): return [[] for _ in range(N)]
def indist(N, s): return [(s) for _ in range(N)]
def inseen(N): return [(False) for _ in range(N)]

# 定数ちゃん
# MOD = 998244353
# MOD = 1000000007
# INF = 10 ** 18 + 1

def bfs(children, parents, ischosen, N):
    # to check 
    leaf = deque([])
    deg = indist(N, 0)
    for v in range(N):
        deg[v] = len(children[v])
        if deg[v] == 0:
            leaf.append(v)
    
    while len(leaf) > 0:
        v = leaf.popleft()
        # 子頂点が一つでも選ばれているか
        flag = False 
        for v2 in children[v]:
            # or 
            flag = flag | ischosen[v2]
        
        # if alr chosen, the par is false 
        # if not yet chosen, choose par
        ischosen[v] = not flag

        # for parent of v 
        p = parents[v]
        deg[p] -= 1 
        if deg[p] == 0:
            leaf.append(p)
    
    return 

def main():
    N = inint()
    graph = ingraph(N)
    for i in range(N-1):
        a, b = inmap()
        graph[a].append(b)
        graph[b].append(a) 
    
    # let the root be 0 
    r = 0 

    children = ingraph(N)
    parents = indist(N, -1)
    seen = inseen(N)
    que = deque()
    seen[r] = True
    parents[r] = r
    que.append(r)

    while len(que) > 0:
        v = que.popleft()

        for v2 in graph[v]:
            if seen[v2]:
                continue 
            seen[v2] = True 
            children[v].append(v2)
            parents[v2] = v
            que.append(v2)
    
    ischosen = inseen(N)
    bfs(children, parents, ischosen, N)

    ans = 0
    for v in range(N):
        if ischosen[v]:
            ans += 1 
    
    return ans 

print(main())



