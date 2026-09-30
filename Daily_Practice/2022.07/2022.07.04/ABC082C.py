from collections import deque, Counter, defaultdict
from operator import itemgetter 
from bisect import bisect_right, bisect_left 
from itertools import combinations, permutations, accumulate, product
import heapq
# from numpy import base_repr
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
    N = int(input())
    A = list(map(int, input().split()))
    B = Counter(A)
    ans = 0
    for key, value in B.items():
        if key > value:
            ans += value
        elif key < value:
            ans += value - key
        else:
            continue    
    return ans

print(main())