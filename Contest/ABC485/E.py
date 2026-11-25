# ABC485E
# https://atcoder.jp/contests/abc485/tasks/abc485_e

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


def main():
    # 直前と同じ色は使えないので、2用意する
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v, c = map(int, input().split())
        G[u-1].append((v-1,c))

    seen = [[] for _ in range(N)]
    seen[0] = [0,0]

    # 頂点、距離、色
    q = deque([(0, 0, 0)])
    # bfs 
    while q:
        u, dist, color = q.popleft()
        for v, c in G[u]:
            if c == color:
                continue 
            if (seen[v][1:]) or c in seen[v]:
                # 被りなのでいらない
                continue 
            if v == N-1:
                print(dist+1)
                return
            seen[v].append(c)
            q.append((v, dist+1, c))

    print(-1)


main()