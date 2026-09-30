from collections import deque, Counter, defaultdict
from operator import itemgetter 
from bisect import bisect_right, bisect_left 
from itertools import combinations, permutations, accumulate, product
import heapq
# from numpy import base_repr
from copy import deepcopy
import sys
# sys.setrecursionlimit(10**6)
from math import gcd
def my_lcm(a, b):
    return a * b // gcd(a, b)
def my_ceil(N, W):
    return (-(-N//W))
def printout(func):
    if func: print("Yes")
    else: print("No")

# MOD = 998,244,353
# MOD = 1,000,000,007

INF = 10 ** 9 + 1 

def main():
    N, W = map(int, input().split())
    weight = []
    value = []
    for _ in range(N):
        w, v = map(int, input().split())
        weight.append(w)
        value.append(v)
    
    dp = [[(INF) for _ in range(100001)] for _ in range(N+1)]
    dp[0][0] = 0
    for row in range(N):
        for col in range(100001):
            if dp[row][col] == INF:
                continue 
            dp[row+1][col] = min(dp[row][col], dp[row+1][col])
            if col + value[row] <= sum(value):
                dp[row+1][col+value[row]] = min(dp[row+1][col+value[row]], dp[row][col] + weight[row])
    
    ans = 0
    # print(dp)
    for i in reversed(range((100001))):
        if dp[-1][i] != INF:
            ans = i+1
            break
    
    return ans

print(main())
