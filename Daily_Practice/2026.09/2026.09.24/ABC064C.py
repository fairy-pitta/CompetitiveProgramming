# ABC064C  茶 (diff 559 / 200pt)
# https://atcoder.jp/contests/abc064/tasks/abc064_c




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
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    b_set = set(B)
    ans1 = 0
    ans2 = 0

    for i in range(N):
        if A[i] == B[i]:
            ans1 += 1 
        elif A[i] in b_set:
            ans2 += 1 

    print(ans1)
    print(ans2)

    return

main()