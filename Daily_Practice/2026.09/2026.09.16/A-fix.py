


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
    d = defaultdict(list)

    #インデックスを見るのでそっちをvalueとして保持
    for i in range(N):
        d[A[i]].append(i)

    # 全ての五の倍数に対して、indexをとって、そのindexより前もしくは後の3,5の同倍数のペアを探す
    
    cnt = 0

    for j in range(N):
        if not A[j] % 5:
            mul = A[j] // 5 
            target_3 = mul * 3 
            target_7 = mul * 7 

            three_list = d[target_3]
            seven_list = d[target_7]
            if not three_list or not seven_list:
                continue

            # ここでindexのリストは手に入ったので、あとは五の倍数のindexに対して
            # それより前もしくは後ろであるものを二分炭酸くで探せばいい

            three_before = bisect_left(three_list, j)
            seven_before = bisect_left(seven_list, j)
            three_after = len(three_list) - three_before 
            seven_after = len(seven_list) - seven_before
            cnt += three_before * seven_before + three_after * seven_after

    return cnt 

print(main())
        
            

