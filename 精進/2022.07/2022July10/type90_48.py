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
    
N, K = map(int, input().split())
AB = []

for i in range(N):
    a, b = map(int, input().split())
    AB.append(b)
    AB.append(a-b)

AB = sorted(AB, reverse = True)
ans = 0
for i in range(K):
    # print(AB[i])
    ans += AB[i]

print(ans)

