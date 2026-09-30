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
MOD = 1000000007
INF = 10 ** 9 + 7
    

def main():
    N, K = map(int, input().split())

    if K == 1:
        if N == 1:
            return 1 
        else:
            return 0
    elif K == 2:
        if N == 1:
            return 2 
        elif N == 2:
            return 2
        else:
            return 0
    else:
        if N == 1:
            return K % MOD
        elif N == 2:
            return K * (K-1) % MOD
        else:
            ans = K * (K-1) * pow(K-2, N-2, MOD) % MOD
            return ans 

print(main())            


