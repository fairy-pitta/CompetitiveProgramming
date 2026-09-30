# ライブラリさんたち
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
from functools import lru_cache
# @lru_cache(maxsize=None)

# 便利な関数くん
def my_lcm(a, b):
    return a * b // gcd(a, b)
def my_ceil(N, W):
    return (-(-N//W))
def out(func):
    if func: print("Yes")
    else: print("No")
import sys
def input(): return sys.stdin.readline()[:-1]
def isint(): return int(input())
def ismap(): return map(int, input().split())
def islist(): return list(input())
def isgraph(N): return [[] for _ in range(N)]
def isdist(N, s): return [(s) for _ in range(N)]
def isseen(N): return [(False) for _ in range(N)]
def iszero(): return list(map(lambda x: int(x) - 1, input().split()))
def sout(list):
    for i in list:
        print(i)

# run-length 
# A = [(k, len(list(g))) for k, g in groupby(map(int, input().split()))]

# 定数ちゃん
# MOD = 998244353
# MOD = 1000000007
# INF = 10 ** 16

def enum_divisors(n):
    """約数列挙 O(√N)"""

    divs_smaller = []
    divs_larger = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divs_smaller.append(i)
            divs_larger.append(n // i)
        i += 1

    if divs_smaller[-1] == divs_larger[-1]:
        divs_smaller.pop()

    divisors = divs_smaller + divs_larger[::-1]

    return divisors


def main():
    K = isint()
    li = enum_divisors(K)
    ans = 0
    n = len(li)
    for i in range(n):
        for j in range(i, n):
            if not K % (li[i] * li[j]) == 0:
                continue 
            c = K // (li[i] * li[j])
            if not li[j] <= c:
                continue 
            # print(li[i], li[j], c)
            ans += 1
    
    return ans 

print(main())
