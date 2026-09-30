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
    # print(B)
    ans = []
    for key, value in B.items():
        if value >= 4:
            ans.append(key)
            ans.append(key)
        elif value >= 2:
            ans.append(key)
        else:
            continue 
    
    ans.sort()
    if len(ans) >= 2:
        return ans[-1] * ans[-2]
    else:
        return 0

print(main())

    


