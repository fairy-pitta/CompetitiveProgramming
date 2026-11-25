# ABC468D  茶 (diff 683 / 200pt)
# https://atcoder.jp/contests/abc468/tasks/abc468_d

# Library: https://github.com/fairy-pitta/CompetitiveProgramming/tree/main/Library

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
def isint(): return int(input())                        # 整数 1 つ
def ismap(): return map(int, input().split())           # 空白区切りの整数 (a, b = ismap())
def issmap(): return map(str, input().split())          # 空白区切りの文字列
def islist(): return list(input())                      # 文字列を 1 文字ずつのリストに
def iszero(): return [int(x) - 1 for x in input().split()]   # 1-indexed を 0-indexed へ


## 出力ヘルパー
def out(cond): print("Yes" if cond else "No")
def sout(xs):                                           # 1 要素ずつ改行して出力
    for x in xs:
        print(x)


## よく使う小道具
def my_lcm(a, b): return a * b // gcd(a, b)             # 最小公倍数
def my_ceil(N, W): return -(-N // W)                    # N / W の切り上げ (float を使わない)
def isgraph(N): return [[] for _ in range(N)]           # 空の隣接リスト
def isdist(N, v): return [v] * N                        # 全部 v で初期化した距離配列
def isseen(N): return [False] * N                       # 訪問済みフラグ

# ランレングス圧縮
# A = [(k, len(list(g))) for k, g in groupby(map(int, input().split()))]


## 定数
# MOD = 998244353
# MOD = 1000000007
# INF = 10 ** 18 + 1


# 各中心から左右に広げ、不一致が 2 回目になる直前までが良い文字列
# 不一致位置はローリングハッシュ + 二分探索の LCE で O(log N) で飛ばす
S = input()
N = len(S)
R = S[::-1]
MOD = (1 << 61) - 1
B = 10 ** 9 + 7
pw = [1] * (N + 1)
hs = [0] * (N + 1)
hr = [0] * (N + 1)
for i in range(N):
    pw[i + 1] = pw[i] * B % MOD
    hs[i + 1] = (hs[i] * B + ord(S[i])) % MOD
    hr[i + 1] = (hr[i] * B + ord(R[i])) % MOD


def get(h, l, r):
    return (h[r] - h[l] * pw[r - l]) % MOD


def lce(l, r):
    """S[l], S[l-1], ... と S[r], S[r+1], ... が何文字一致するか"""
    if l < 0 or r >= N:
        return 0
    p = N - 1 - l
    ok, ng = 0, min(l + 1, N - r) + 1
    while ng - ok > 1:
        m = (ok + ng) // 2
        if get(hs, r, r + m) == get(hr, p, p + m):
            ok = m
        else:
            ng = m
    return ok


def count(l, r):
    """中心 (l, r) から広げたときの良い文字列の個数"""
    mx = min(l + 1, N - r)
    k1 = lce(l, r)
    if k1 == mx:
        return mx
    # 1 回目の不一致は書き換えで許す
    return k1 + 1 + lce(l - k1 - 1, r + k1 + 1)


ans = 0
for c in range(N):
    ans += 1 + count(c - 1, c + 1)   # 奇数長
    ans += count(c, c + 1)           # 偶数長
print(ans)
