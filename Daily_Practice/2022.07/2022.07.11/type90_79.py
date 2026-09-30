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
    H, W = i_map()
    A = []
    B = []
    for _ in range(H):
        a = list(i_map())
        A.append(a)
    for _ in range(H):
        b = list(i_map())
        B.append(b)
    
    op = 0
    for row in range(H-1):
        for col in range(W-1):
            diff = B[row][col] - A[row][col]
            if diff == 0:
                continue 
            if diff > 0:
                op += diff 
                A[row+1][col] += diff
                A[row+1][col+1] += diff 
                A[row][col+1] += diff
            else:
                op += abs(diff)
                A[row+1][col] += diff
                A[row+1][col+1] += diff 
                A[row][col+1] += diff
    
    # print(A)
    # print(B)
    if A[H-1][W-1] == B[H-1][W-1]:
        print("Yes")
        print(op)
    else:
        print("No")

main()
            




