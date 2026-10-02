# ABC232D  茶 (diff 539 / 200pt)
# https://atcoder.jp/contests/abc232/tasks/abc232_d

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
    H, W = ismap()
    grid = []
    for _ in range(H):
        r = input()
        grid.append(r)

    start = (0, 0)
    # 下か右しか行けない
    # いけるところにseenをつけていき、dequeueに追加していくBFS
    seen = [[False] * W for _ in range(H)]
    dist = [[0] * W for _ in range(H)]

    seen[0][0] = True
    dist[0][0] = 1          # マス (0,0) 自身を 1 歩目として数える
    q = deque([start])
    ans = 1

    while q:
        h, w = q.popleft()
        ans = max(ans, dist[h][w])
        for nh, nw in ((h + 1, w), (h, w + 1)):   # 下・右のみ
            if nh >= H or nw >= W:
                continue
            if grid[nh][nw] == "#":
                continue
            if seen[nh][nw]:
                continue
            seen[nh][nw] = True
            dist[nh][nw] = dist[h][w] + 1
            q.append((nh, nw))

    print(ans)
    return


main()
