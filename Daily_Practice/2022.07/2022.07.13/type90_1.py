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
# INF = 10 ** 9 + 1 

def i_int(): return int(input())
def i_map(): return map(int, input().split())


def main():
    N, L = i_map()
    K = i_int()
    A = list(i_map())

    def judge(m):
        cnt = 0
        last_pos = 0
        
        for i in range(N):
            if A[i] - last_pos >= m and L - A[i] >= m:
                cnt += 1
                last_pos = A[i]
        
        if cnt >= K:
            return True 
        else:
            return False 
    
    left = -1 
    right = L+1 
    while abs(right - left) > 1:
        mid = (right + left) // 2
        if judge(mid):
            left = mid 
        else:
            right = mid 
    
    print(left)
    


