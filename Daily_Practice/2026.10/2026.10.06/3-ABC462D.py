# ABC462D  茶 (diff 798 / 200pt)
# https://atcoder.jp/contests/abc462/tasks/abc462_d

## frequently used imports
from collections import deque, Counter, defaultdict
from operator import itemgetter
from bisect import bisect_right, bisect_left
from itertools import combinations, permutations, accumulate, product, groupby
from copy import deepcopy
from math import gcd, log2, log10
from functools import lru_cache, reduce
import heapq
import sys
# sys.setrecursionlimit(10**9)


## 入力ヘルパー
# 大量入力のときは input を差し替える
# def input(): return sys.stdin.readline().rstrip("\n")
def isint(): return int(input())
def ismap(): return map(int, input().split())
def issmap(): return map(str, input().split())
def islist(): return list(input())
def iszero(): return [int(x) - 1 for x in input().split()]   # 1-indexed を 0-indexed へ


## 出力ヘルパー
def out(cond): print("Yes" if cond else "No")
def sout(xs):
    for x in xs:
        print(x)


## よく使う小道具
def my_lcm(a, b): return a * b // gcd(a, b)
def my_ceil(N, W): return -(-N // W)
def isgraph(N): return [[] for _ in range(N)]
def isdist(N, v): return [v] * N
def isseen(N): return [False] * N

# ランレングス圧縮
# A = [(k, len(list(g))) for k, g in groupby(map(int, input().split()))]


## 定数
# MOD = 998244353
# MOD = 1000000007
# INF = 10 ** 18 + 1

from operator import mul
from functools import reduce

def cmb(n,r):
    if n <= 1: return 0
    r = min(n-r,r)
    if r == 0: return 1
    nume = reduce(mul, range(n, n - r, -1))
    denom = reduce(mul, range(1, r + 1))
    return nume // denom

def main():
    N, D = map(int, input().split())
    maximum = 10 ** 6 + 2 
    imos = [0] * maximum 

    for _ in range(N):
        s, t = map(int, input().split())
        r = t - D 

        if s <= r: 
            imos[s] += 1 
            imos[r+1] -= 1 

    ans = 0
    cnt = 0

    for i in range(maximum):
        cnt += imos[i]
        ans += cmb(cnt, 2)

    print(ans)
    return 

main()



