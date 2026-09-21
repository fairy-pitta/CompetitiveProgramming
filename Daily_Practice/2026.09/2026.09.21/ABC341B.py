# ABC341B  0-100 (diff 42 / 100pt)
# https://atcoder.jp/contests/abc341/tasks/abc341_b




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
    L, R = map(int, input().split())

    if R - L >= 2018:
        return 0

    ans = 10**18
    for l in range(L, R):
        for r in range(l+1, R+1):
            ans = min(ans, (l*r)%2019)

    return ans 

print(main())

    

