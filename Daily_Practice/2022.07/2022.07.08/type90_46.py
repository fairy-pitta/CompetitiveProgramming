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
    MOD = 46
    N = int(input())
    A = list(map(int, input().split())) 
    B = list(map(int, input().split())) 
    C = list(map(int, input().split()))
    A_new = []
    B_new = []
    C_new = []
    for k in range(N):
        A_new.append(A[k] % MOD)
        B_new.append(B[k] % MOD)
        C_new.append(C[k] % MOD)
    
    A_num = Counter(A_new)
    B_num = Counter(B_new)
    C_num = Counter(C_new)

    ans = 0
    for i, j in A_num.items():
        for k, l in B_num.items():
            for p, q in C_num.items():
                if (i + k + p) % MOD == 0:
                    ans += (j * l * q)

    return ans 

print(main())
