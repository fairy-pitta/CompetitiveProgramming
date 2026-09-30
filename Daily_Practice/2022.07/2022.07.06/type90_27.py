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

# MOD = 998,244,353
# MOD = 1,000,000,007
# INF = 10 ** 9 + 1 

def main():
    N = int(input())
    names = set()
    for i in range(1, N+1): 
        s = str(input())
        if s not in names:
            print(i)
            names.add(s)
        else:
            continue

main()
