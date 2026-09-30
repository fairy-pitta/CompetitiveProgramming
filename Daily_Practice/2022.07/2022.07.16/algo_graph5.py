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


def b_judge(now, graph, color, stack):
    while len(stack) > 0:
        now = stack.popleft()
        for v2 in graph[now]:
            if color[v2] != -1:
                if color[v2] == color[now]:
                    return False 
                else:
                    continue 
            color[v2] = 1 - color[now]
            stack.append(v2)
    
    return True 
             

def main():
    N, M = inmap()
    graph = [[] for _ in range(N)]
    color = [(-1) for _ in range(N)]
    for _ in range(M):
        a, b = inmap()
        graph[a].append(b)
        graph[b].append(a)

    ans = True 
    for point in range(N):
        if color[point] != -1:
            continue 
        color[point] = 1 
        stack = deque()
        stack.append(point) 
        if not b_judge(point, graph, color, stack):
            ans = False
    
    return ans

out(main())
        

