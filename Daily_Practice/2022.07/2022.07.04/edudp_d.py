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

def main():
    N, W = map(int, input().split())
    weight = []
    value = []
    for _ in range(N):
        w, v = map(int, input().split())
        weight.append(w)
        value.append(v)
    dp = [[(-1) for _ in range(W+1)] for _ in range(N+1)]
    dp[0][0] = 0
    for row in range(N):
        for col in range(W+1):
            if dp[row][col] == -1:
                continue 
            if dp[row+1][col] == -1:
                dp[row+1][col] = dp[row][col]
            else:
                dp[row+1][col] = max(dp[row+1][col], dp[row][col])
            
            if col + weight[row] <= W:
                if dp[row+1][col+weight[row]] == -1:
                    dp[row+1][col+weight[row]] = dp[row][col] + value[row]
                else:
                    dp[row+1][col+weight[row]] = max(dp[row][col] + value[row], dp[row+1][col+weight[row]])
    # print(dp)
    return max(dp[-1])

print(main())