# ABC046B  茶 (diff 633 / 200pt)
# https://atcoder.jp/contests/abc046/tasks/abc046_b




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
    N, M, T = map(int, input().split())
    A = [0] + list(map(int, input().split()))
    bonus = defaultdict(int)
    for k in range(M):
        x,y = map(int, input().split())
        bonus[x] = y

    print(A)
    room = 1

    while True:
        if room == N:
            break
        if T < A[room]:
            break 
        T -= A[room]
        room += 1
        T += bonus[room]
        # print(T, room, bonus)

    if room == N:
        print("Yes")
    else:
        print("No")

main()

        
