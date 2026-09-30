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
    A = sorted(list(map(int, input().split())))
    Q = int(input())
    for student in range(Q):
        b = int(input())
        ind = bisect_right(A, b)
        if ind == 0:
            dis = abs(A[ind] - b)
        elif ind == len(A):
            dis = abs(A[-1] - b)
        else:
            dis = min(abs(A[ind-1] - b), abs(A[ind] - b))
            
        print(dis)

main()
