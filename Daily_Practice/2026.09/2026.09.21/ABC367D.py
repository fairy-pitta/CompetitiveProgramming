# ABC367D  緑 (diff 1037 / 300pt)
# https://atcoder.jp/contests/abc367/tasks/abc367_d




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
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))

    MOD = 998244353

    # 順番関係ないのでソートしておく
    # 累積和が使える？
    # にぶたんで切って、下はB*num-sum, 上はsum - B*numで足せば計算自体はO(1)でいけそう

    A_acc = []
    a_term = 0
    for i in range(N):
        a_term += A[i]
        A_acc.append(a_term)

    B_acc = []
    b_term = 0
    for j in range(M):
        b_term += B[j]
        B_acc.append(b_term)


    ans = 0

    for k in range(M):
        idx = bisect_left(A, B[k])  
        smaller_sum = A_acc[idx-1] if idx > 0 else 0  
        bigger_sum = A_acc[-1] - smaller_sum 
        ans += B[k] * idx - smaller_sum 
        ans += bigger_sum - B[k] * (N-idx)
        ans %= MOD

    return ans % MOD

print(main())
