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
def isint(): return int(input())
def ismap(): return map(int, input().split())
def islist(): return list(input())
def isgraph(N): return [[] for _ in range(N)]
def isdist(N, s): return [(s) for _ in range(N)]
def isseen(N): return [(False) for _ in range(N)]

# 定数ちゃん
# MOD = 998244353
# MOD = 1000000007
# INF = 10 ** 18 + 1


def main():
    N = isint()
    graph = isgraph(N)
    for _ in range(N-1):
        a, b = ismap()
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    num = N // 2 
    dist = isdist(N, -1)
    start = 0 
    stack = deque()
    stack.append(start)
    dist[start] = 1
    color = [0, 1]
    one = []
    one.append(1)
    zero = []
    while len(stack) > 0:
        v = stack.popleft()
        for v2 in graph[v]:
            if dist[v2] != -1:
                continue 
            dist[v2] = 1 - dist[v]
            color[1 - dist[v]] += 1 
            stack.append(v2)
            if dist[v2] == 0:
                zero.append(v2 + 1)
            elif dist[v2] == 1:
                one.append(v2+1)
    ans = []
    for i in range(num):
        if color[0] >= color[1]:
            ans.append(zero[i])
        else:
            ans.append(one[i])
    
    # print(one)
    # print(zero)
    print(*ans)

main()
    

        