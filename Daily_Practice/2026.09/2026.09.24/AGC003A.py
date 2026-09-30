# AGC003A  茶 (diff 436 / 200pt)
# https://atcoder.jp/contests/agc003/tasks/agc003_a




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
def input(): return sys.stdin.readline()[:-1]


def main():
    Q = int(input())

    d = deque()
    h = []
    ans = []

    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            d.append(query[1])
        elif query[0] == 2:
            if len(h) > 0:
                ans.append(heapq.heappop(h))
            else:
                ans.append(d.popleft())
        else:
            while d:
                heapq.heappush(h, d.popleft())

    for j in ans:
        print(j)

    return

main()
