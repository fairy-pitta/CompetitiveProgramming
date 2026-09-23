# ABC159D  茶 (diff 496 / 200pt)
# https://atcoder.jp/contests/abc159/tasks/abc159_d




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
    A = [input() for _ in range(N)]
    B = [input() for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if A[i][j] != B[i][j]:
                print(i+1, j+1)
                return

    return

main()