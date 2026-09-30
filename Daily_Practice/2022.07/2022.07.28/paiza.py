# ライブラリさんたち
from collections import deque, Counter, defaultdict
from operator import itemgetter 
from bisect import bisect_right, bisect_left 
from itertools import combinations, permutations, accumulate, product, groupby
import heapq
# from numpy import base_repr
from copy import deepcopy
import sys
# sys.setrecursionlimit(10**9)
from math import gcd, log2, log10
from functools import lru_cache
# @lru_cache(maxsize=None)

# 便利な関数くん
def my_lcm(a, b):
    return a * b // gcd(a, b)
def my_ceil(N, W):
    return (-(-N//W))
def out(func):
    if func: print("Yes")
    else: print("No")
import sys
def input(): return sys.stdin.readline()[:-1]
def isint(): return int(input())
def ismap(): return map(int, input().split())
def issmap(): return map(str, input().split())
def islist(): return list(input())
def isgraph(N): return [[] for _ in range(N)]
def isdist(N, s): return [(s) for _ in range(N)]
def isseen(N): return [(False) for _ in range(N)]
def iszero(): return list(map(lambda x: int(x) - 1, input().split()))
def sout(list):
    for i in list:
        print(i)

# run-length 
# A = [(k, len(list(g))) for k, g in groupby(map(int, input().split()))]

# 定数ちゃん
# MOD = 998244353
# MOD = 1000000007
# INF = 10 ** 16


def main():
    N, M = ismap()
    field = [[] for _ in range(M)]
    start = 0
    goal = 0
    for i in range(M):
        s = list(map(str, input().split()))
        for j in range(N):
            if s[j] == 's':
                start = (i, j)
            elif s[j] == 'g':
                goal = (i, j)
            field[i].append(s[j])
    
    stack = deque()
    stack.append(start)
    direc = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    dp = [[(-1) for _ in range(N)] for _ in range(M)]
    start_r, start_c = start 
    dp[start_r][start_c] = 0
    while len(stack) > 0:
        now_r, now_c = stack.popleft()
        for i in direc:
            togo_r, togo_c = i
            r = now_r + togo_r 
            c = now_c + togo_c 
            if 0 <= r <= M-1 and 0 <= c <= N-1:
                if field[r][c] == "0" or field[r][c] == "g":
                    if dp[r][c] == -1:
                        dp[r][c] = dp[now_r][now_c] + 1 
                        stack.append((r,c))
                    else:
                        continue 
                else:
                    continue 
            else:
                continue 
    
    goal_r, goal_c = goal 
    if dp[goal_r][goal_c] != -1:
        return dp[goal_r][goal_c]
    else:
        return "Fail"

print(main())


        

                
                

