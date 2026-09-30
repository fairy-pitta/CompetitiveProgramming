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
    N, K = ismap()
    A = list(ismap())
    d = defaultdict(int)
    left = 0
    right = 0
    d[A[0]] += 1
    gap = right - left + 1
    # print(d)
    while True:
        if len(d) <= K:
            right += 1 
            d[A[right]] += 1 
            if len(d) <= K:
                gap = max(gap, right - left + 1)
    

        elif len(d) > K:
            d[A[left]] -= 1 
            if d[A[left]] == 0:
                d.pop(A[left])
            left += 1
        
        # print(d)
        # print(left, right)


        if right == N-1:
            break 
        if left == N-1:
            break
    return gap

print(main())
        
