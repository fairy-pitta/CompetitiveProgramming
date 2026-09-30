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


def main():
    N, Q = i_map()
    A = list(i_map())
    gap = []
    s = 0
    for i in range(N-1):
        gap.append(A[i+1] - A[i])
        s += abs(A[i+1] - A[i])
    
    for _ in range(Q):
        L, R, V = i_map()
        L -= 1
        R -= 1
        if L == 0 and R == N-1:
            print(s)
        elif L == 0:
            s -= abs(gap[R])
            gap[R] -= V
            s += abs(gap[R])
            print(s)
        elif R == N-1:
            s -= abs(gap[L-1])
            gap[L-1] += V
            s += abs(gap[L-1])
            print(s)
        else:
            s -= abs(gap[R])
            s -= abs(gap[L-1])
            gap[R] -= V
            gap[L-1] += V
            s += abs(gap[R]) + abs(gap[L-1])
            print(s)

main()




            




