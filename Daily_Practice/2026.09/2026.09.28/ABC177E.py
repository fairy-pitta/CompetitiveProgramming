# ABC177E  緑 (diff 1057 / 300pt)
# https://atcoder.jp/contests/abc177/tasks/abc177_e




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
    A = list(map(int, input().split()))
    B = set(list(map(int, input().split())))


    food = []
    max_oishisa = max(A)
    for i in range(N):
        if A[i] == max_oishisa:
            food.append(i)

    flag = False
    for j in food:
        if j+1 in B:
            flag = True

    if flag:
        print("Yes")
    else:
        print("No")

main()
