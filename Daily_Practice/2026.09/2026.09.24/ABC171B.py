# ABC171B  灰 (diff 0 / 100pt)
# https://atcoder.jp/contests/abc171/tasks/abc171_b




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
    N, K = map(int, input().split())
    p = sorted(list(map(int, input().split())))

    print(sum(p[:K]))
    return

main()