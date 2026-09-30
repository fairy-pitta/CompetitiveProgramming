# ABC243B  0-100 (diff 0 / 100pt)
# https://atcoder.jp/contests/abc243/tasks/abc243_b




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


#######
# レート 
# 1-
# 399：灰色
# レート 
# 400-
# 799：茶色
# レート 
# 800-
# 1199：緑色
# レート 
# 1200-
# 1599：水色
# レート 
# 1600-
# 1999：青色
# レート 
# 2000-
# 2399：黄色
# レート 
# 2400-
# 2799：橙色
# レート 
# 2800-
# 3199：赤色
#######

def main():
    N = int(input())
    a = list(map(int, input().split()))
    d = defaultdict(int)

    for i in range(N):
        rate = a[i]
        if rate < 400:
            d["grey"] += 1 
        elif rate < 800:
            d["brown"] += 1 
        elif rate < 1200:
            d["green"] += 1 
        elif rate < 1600:
            d["skyblue"] += 1 
        elif rate < 2000:
            d["blue"] += 1 
        elif rate < 2400:
            d["yellow"] += 1 
        elif rate < 2800:
            d["orange"] += 1 
        elif rate < 3200:
            d["red"] += 1
        else:
            d["master"] += 1 

    ans = 0
    for key, value in d.items():
        if key != "master":
            ans += 1

    if len(d) == 1 and d["master"]:
        print(1, d["master"])
    elif d["master"] > 0:
        print(ans, ans+d["master"])
    else:
        print(ans, ans)

    # print(d) 

    return 

main()

    