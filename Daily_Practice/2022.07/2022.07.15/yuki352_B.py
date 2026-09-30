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

# 定数ちゃん
# MOD = 998244353
MOD = 10 ** 9 + 7
# INF = 10 ** 18 + 1

def main():
    N = inint()
    A = list(inmap())
    B = list(inmap())
    li = []
    for i in range(N):
        li.append([A[i], B[i]])
    
    li = sorted(li, key = itemgetter(0))
    print(li)
    ans = 0
    level = 1 
    for j in range(N):
        ans += level * li[j][0] % MOD
        level = level * li[j][1]
    
    return ans % MOD

print(main())


