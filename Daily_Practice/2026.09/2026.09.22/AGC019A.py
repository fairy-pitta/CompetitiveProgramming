# AGC019A  茶 (diff 509 / 200pt)
# https://atcoder.jp/contests/agc019/tasks/agc019_a




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
    Q,H,S,D = map(int, input().split())
    N = int(input())
    # 0.25と0.5はどうせ1にして使わないといけない
    one_litre = min(Q*4, H*2, S)

    cost = 0
    if one_litre * 2 > D:
        cost += (N // 2) * D
        cost += (N % 2) * one_litre 

    else:
        cost += one_litre * N

    print(cost)

main()