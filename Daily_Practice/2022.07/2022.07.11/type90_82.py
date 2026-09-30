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
# INF = 10 ** 9 + 1 

def i_int(): return int(input())
def i_map(): return map(int, input().split())


def ketasu(n):
    keta = len(str(n))
    s = 0
    for i in range(1, keta+1):
        if i != keta:
            # first number 
            first = 10 ** (i-1)
            # last number  
            last = 10 ** i - 1
            # sum 
            tmp = (first + last) * (last - first + 1) // 2
            # multiply 
            s += tmp * i
        else:
            first = 10 ** (i-1)
            last = n
            tmp = (first + last) * (last - first + 1) // 2
            s += tmp * i
    
    return s 

def main():
    L, R = i_map()
    return (ketasu(R) - ketasu(L-1)) % MOD

print(main())


            




