# ABC241D  緑 (diff 1177 / 300pt)
# https://atcoder.jp/contests/abc241/tasks/abc241_d




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

from operator import mul
from functools import reduce

def cmb(n,r):
    if n <= 1: return 0 
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under



def main():
    N = int(input())
    A = list(map(int, input().split()))
    d = defaultdict(int)

    for i in range(N):
        d[A[i]] += 1

    all_scenario = 0
    for value in d.values():
        all_scenario += cmb(value, 2)

    for j in range(N):
        chance = cmb(d[A[j]], 2) - cmb((d[A[j]]-1), 2)
        print(all_scenario - chance)

    return

main()
