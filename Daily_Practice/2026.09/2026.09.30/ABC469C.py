# ABC469C  茶 (diff 475 / 200pt)
# https://atcoder.jp/contests/abc469/tasks/abc469_c




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
    S = input()
    r = []
    for i in range(N):
        if i == 0 and S[i] == "o":
            r.append(0)
        elif i == 0 and S[i] == "x":
            r.append(1)
        elif S[i] == "x":
            r.append(r[-1]+1)
        else:
            r.append(r[-1])
    print(r)
    for j in range(1,N+1):
        idx = bisect_left(r, j)
        if idx == len(S):
            print(idx)
        else:
            print(idx+1)

main()