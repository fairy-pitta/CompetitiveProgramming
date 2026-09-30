from collections import deque, Counter, defaultdict
from operator import itemgetter 
from bisect import bisect_right, bisect_left 
from itertools import combinations, permutations, accumulate, product
import heapq
from copy import deepcopy
import sys
sys.setrecursionlimit(10**6)
from math import gcd
def my_lcm(a, b):
    return a * b // gcd(a, b)
def my_ceil(N, W):
    return (-(-N//W))
def printout(func):
    if func: print("Yes")
    else: print("No")


def main():
    N, M = map(int, input().split())
    pages = []
    days = []
    for _ in range(N):
        b, x = map(int, input().split())
        pages.append(b)
        days.append(x)
    dp = [[(-1) for _ in range(M+1)] for _ in range(N+1)]
    dp[0][0] = 0
    m = 0
    for book in range(N):
        for day in range(M+1):
            if dp[book][day] == -1:
                continue 
            dp[book+1][day] = max(dp[book+1][day], dp[book][day])
            m = max(m, dp[book+1][day])
            if day + days[book] <= M:
                dp[book+1][day + days[book]] = max(dp[book+1][day + days[book]], dp[book][day] + pages[book])
                m = max(m, dp[book+1][day + days[book]])
    # print(dp)
    return m

print(main())
    
