from collections import deque, Counter, defaultdict
from operator import itemgetter 
from bisect import bisect_right, bisect_left 
from itertools import combinations, permutations, accumulate, product
import heapq
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
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    dp = [(-1) for _ in range(N)]
    dp[0] = 0
    for i in range(N):
        if dp[i] == -1:
            continue 
        for k in range(1, K+1):
            j = i + k 
            if j < N:
                cost = abs(H[j] - H[i])
                if dp[j] == -1:
                    dp[j] = dp[i] + cost
                else:
                    dp[j] = min(dp[j], dp[i] + cost)
    
    # print(dp)
    return dp[-1]

print(main())
