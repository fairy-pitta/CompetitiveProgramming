# ABC192C  灰 (diff 0 / 100pt)
# https://atcoder.jp/contests/abc192/tasks/abc192_c




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
 

def calc(n):
    g1 = int("".join(reversed(sorted(str(n)))))
    g2 = int("".join(sorted(str(n))))

    return g1 - g2 


def main():
    N, K = map(int, input().split())

    term = N

    for i in range(K):
        term = calc(term)

    return term


print(main())