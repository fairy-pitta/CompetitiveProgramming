from collections import deque, Counter, defaultdict
from operator import itemgetter 
from bisect import bisect_right, bisect_left 
from itertools import combinations, permutations, accumulate, product
import heapq
from numpy import base_repr
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

# adjacency list 
N = int(input())
mastered = [False] * N
A, T = [], []
ans = 0

for _ in range(N):
    t, k, *a = map(int, input().split())
    T.append(t)
    if k == 0:
        A.append([])
    else:
        A.append(list(a))

stack = [N-1]
