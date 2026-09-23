# ABC204C  茶 (diff 629 / 200pt)
# https://atcoder.jp/contests/abc204/tasks/abc204_c




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
    ruiseki = []
    for i in range(N):
        if i == 0:
            ruiseki.append(A[i])
        else:
            ruiseki.append(ruiseki[i-1] + A[i])

    sum_A = ruiseki[-1]
    ans = 10**18

    for j in range(N-1):
        diff = abs(ruiseki[j] - (sum_A - ruiseki[j]))
        ans = min(ans, diff)

    print(ans)

main()