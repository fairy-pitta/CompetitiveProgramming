# ABC268C  茶 (diff 676 / 200pt)
# https://atcoder.jp/contests/abc268/tasks/abc268_c




## frequently used functions 
from collections import deque, Counter, defaultdict
from operator import itemgetter 
from bisect import bisect_right, bisect_left 
from itertools import combinations, permutations, accumulate, product, groupby
import heapq
# from numpy import base_repr
from copy import deepcopy
import sys
# sys.setrecursionlimit(10**9)
from math import gcd, log2, log10
from functools import lru_cache, reduce 

def main():
    N = int(input())
    t1 = 0
    t2 = 0
    for _ in range(N):
        a,b = map(int, input().split())
        t1 += a
        t2 += b

    if t1 > t2:
        print("Takahashi")
    elif t2 > t1:
        print("Aoki")
    else:
        print("Draw")

main()
