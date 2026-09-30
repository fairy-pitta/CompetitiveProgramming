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
    N, Q = map(int, input().split())
    S = input()

    left = [0]

    for i in range(N):       
        if i > 0 and S[i] == S[i-1]:
            left.append(left[-1]+1)
        else:
            left.append(left[-1]+0)
    
    print(left)
    for _ in range(Q):
        l, r = map(int, input().split())
        print(left[r] - left[l])

    
    
main()