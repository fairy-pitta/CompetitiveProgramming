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
INF = 10 ** 9 + 1 

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    shift = 0
    for turn in range(Q):
        t, x, y = map(int, input().split())
        new_x = (x-1-shift) % N
        new_y = (y-1-shift) % N
        if t == 1:
           A[new_x], A[new_y] = A[new_y], A[new_x]
        elif t == 2:
            shift += 1
        else: 
            print(A[new_x]) 

main()



    