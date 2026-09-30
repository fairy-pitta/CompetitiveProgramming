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
    D = list(map(int, input().split()))

    ans = 0
    for month in range(1, N+1):
        for day in range(1, D[month-1]+1):
            m = list(str(month))
            d = list(str(day))
            li = set(m+d)
            if len(li) == 1:
                ans += 1
    
    print(ans)

main()