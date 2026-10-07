# ABC260C  茶 (diff 413 / 200pt)
# https://atcoder.jp/contests/abc260/tasks/abc260_c

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
    N, X, Y = map(int, input().split())
    # レベル n の赤い宝石 ( n は 2 以上) を「レベル n−1 の赤い宝石 1 個と、レベル n の青い宝石 X 個」に変換する
    # レベル n の青い宝石 ( n は 2 以上) を「レベル n−1 の赤い宝石 1 個と、レベル n−1 の青い宝石 Y 個」に変換する。
    red = [0] * N
    blue = [0] * N
    red[-1] = 1

    # 上のレベルから順に、まとめて全部変換していく
    for level in range(N - 1, 0, -1):
        # 赤(level) -> 赤(level-1) 1個 + 青(level) X個  ※青は同じレベルに出るので先に処理
        cnt = red[level]
        red[level - 1] += cnt
        blue[level] += X * cnt
        red[level] = 0

        # 青(level) -> 赤(level-1) 1個 + 青(level-1) Y個
        cnt = blue[level]
        red[level - 1] += cnt
        blue[level - 1] += Y * cnt
        blue[level] = 0

    print(blue[0])

main()

    


