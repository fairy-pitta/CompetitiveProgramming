# ABC128C  緑 (diff 805 / 300pt)
# https://atcoder.jp/contests/abc128/tasks/abc128_c

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

def main():
    N, M = map(int, input().split())

    # 電球ごとに、つながってるスイッチ番号を0-indexedで持っておく
    bulbs = []
    for _ in range(M):
        k, *s = map(int, input().split())
        bulbs.append([x-1 for x in s])

    P = list(map(int, input().split()))

    # N <= 10 なので 2^N = 1024通りしかない、全部試してOK
    # product で (0,1) の組み合わせを順番に出してもらう
    ans = 0
    for switches in product((0, 1), repeat=N):
        flag = True
        for s, p in zip(bulbs, P):
            # ONのスイッチの個数の偶奇が p と一致してれば点く
            if sum(switches[i] for i in s) % 2 != p:
                flag = False
                break
        if flag:
            ans += 1

    print(ans)
    return

main()
