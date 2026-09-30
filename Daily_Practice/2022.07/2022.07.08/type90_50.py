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
INF = 10 ** 9 + 7

def main():
    N, L = map(int, input().split())
    dp = [(0) for _ in range(N+1)]
    dp[0] = 1
    for i in range(N):
        dp[i+1] += dp[i]
        if i+L <= N:
            dp[i+L] += dp[i]
    
    return dp[-1] % INF

print(main())