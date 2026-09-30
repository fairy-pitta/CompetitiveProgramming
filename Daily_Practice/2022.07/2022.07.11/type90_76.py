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

def main():
    N = int(input())
    A = list(map(int, input().split())) * 2 
    s = (sum(A) // 2)
    outcome = 0
    if s % 10 == 0:
        outcome = s // 10
    else:
        return False
    
    li = list(accumulate(A))
    for start in range(N):
        if start == 0:
            ind = bisect_right(li, outcome)
            if ind-1 < 0:
                continue 
            else:
                if li[ind-1] == outcome:
                    return True
                else:
                    continue 
        else:
            tmp = outcome + li[start-1]
            ind = bisect_right(li, tmp)
            if li[ind-1] == tmp:
                return True
            else:
                continue
                
    
    return False

printout(main())



