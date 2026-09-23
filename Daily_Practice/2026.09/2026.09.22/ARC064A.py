# ARC064A  緑 (diff 1164 / 300pt)
# https://atcoder.jp/contests/arc064/tasks/arc064_a




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
    N, x = map(int, input().split())
    a = list(map(int, input().split()))

    cnt = 0

    for i in range(N-1):
        if a[i] > x:
            cnt += a[i]-x
            a[i] = x 
        if a[i] + a[i+1] > x:
            cnt += (a[i+1] + a[i])-x
            a[i+1] -= (a[i+1] + a[i])-x

    print(cnt)

main()

