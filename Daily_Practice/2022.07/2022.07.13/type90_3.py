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
def my_lcm(a, b):
    return a * b // gcd(a, b)
def my_ceil(N, W):
    return (-(-N//W))
def printout(func):
    if func: print("Yes")
    else: print("No")

# MOD = 998244353
# MOD = 1000000007
# INF = 10 ** 9 + 1 

def i_int(): return int(input())
def i_map(): return map(int, input().split())


# 最短経路の最大値
def bfs_max_dist(start, N, graph):
    # stack を用意、始点を追加
    stack = deque()
    stack.append(start)
    # 始点からの距離を管理
    dist = [(-1) for _ in range(N+1)]
    dist[start] = 0
    # 一番遠い点
    max_point = 0
    # 始点から一番遠い点までの距離
    max_dist = 0
    while len(stack) > 0:
        now = stack.popleft()
        togo = graph[now]
        for point in togo:
            if dist[point] != -1:
                continue 
            elif dist[now] + 1 > max_dist:
                max_point = point 
            
            stack.append(point)
            dist[point] = dist[now] + 1
            max_dist = max(max_dist, dist[now] + 1)
    
    return max_point, max_dist 

            
def main():
    N = i_int()
    graph = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a,b = i_map()
        graph[a].append(b)
        graph[b].append(a)
    
    # 1から一番遠い点
    p, _ = bfs_max_dist(1, N, graph)
    # そこから一番遠い点までの距離
    _, ans = bfs_max_dist(p, N, graph)

    return ans + 1 

print(main())




