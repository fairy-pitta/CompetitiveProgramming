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
    S = deque(list(input()))
    d = deque()

    for _ in range(len(S)):
        item = S.popleft()
        d.append(item)
        if len(d) >= 3 and d[-3] == "A" and d[-2] == "B" and d[-1] == "C":
            d.pop()
            d.pop()
            d.pop()
    
    print("".join(list(d)))

main()
    