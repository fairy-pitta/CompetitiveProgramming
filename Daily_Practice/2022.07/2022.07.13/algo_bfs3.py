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

# 木の直径を求める
# 最短経路の最大値

def main():
    H, W = i_map()
    x, y, p, q = i_map()
    direc = [(1,0), (0,1), (-1, 0), (0, -1)]
    field = []

    for _ in range(H):
        s = list(input())
        field.append(s)
    
    tbl = [[(-1) for _ in range(W)] for _ in range(H)]
    tbl[x][y] = 0
    stack = deque()
    start = (x, y)
    stack.append(start)
    s = set()
    s.add(start)

    while len(stack) > 0:
        now_x, now_y = stack.popleft()
        for i in direc:
            togo_x, togo_y = i
            next_x = togo_x + now_x 
            next_y = togo_y + now_y
            if 0 <= next_x < H and 0 <= next_y < W:
                if tbl[next_x][next_y] == -1 and field[next_x][next_y] == "W":
                    tbl[next_x][next_y] = tbl[now_x][now_y] + 1 
                    stack.append((next_x, next_y))
                else:
                    continue 
            else:
                continue 
        
    # for i in range(H):
    #     print(*tbl[i])
    return tbl[p][q]

print(main())