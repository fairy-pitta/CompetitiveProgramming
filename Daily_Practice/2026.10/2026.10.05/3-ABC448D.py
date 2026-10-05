# ABC448D  茶 (diff 638 / 200pt)
# https://atcoder.jp/contests/abc448/tasks/abc448_d

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
    input = sys.stdin.readline
    N = int(input())

    G = isgraph(N + 1)
    for _ in range(N - 1):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)

    A = [0] + list(map(int, input().split()))  

    ans = [""] * (N + 1)
    cnt = defaultdict(int)   # 現在のパス上に、その値が何個あるか
    dup = 0               

    ## (頂点, 親, True=入る / False=出る)
    stack = [(1, 0, True)]
    while stack:
        v, parent, entering = stack.pop()

        if entering:
            cnt[A[v]] += 1
            if cnt[A[v]] == 2:          # 1→2 になった瞬間だけ加算
                dup += 1
            ans[v] = "Yes" if dup > 0 else "No"

            stack.append((v, parent, False)) 
            for nxt in G[v]:
                if nxt != parent:
                    stack.append((nxt, v, True))
        else:
            if cnt[A[v]] == 2:          # 2→1 に戻る瞬間だけ減算
                dup -= 1
            cnt[A[v]] -= 1

    print("\n".join(ans[1:]))

    return


main()
