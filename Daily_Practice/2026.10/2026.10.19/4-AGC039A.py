# AGC039A  茶 (diff 517 / 200pt)
# https://atcoder.jp/contests/agc039/tasks/agc039_a

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
    S = input()
    K = int(input())

    # 同じ文字がL個続いてるところは、1個飛ばしで書き換えれば隣が同じにならないのでL//2回
    # 真ん中のランはK回出てくるだけなのでK倍
    # 左端と右端は連結したときにくっついて1本のランになるので、そこだけ別で数える
    # くっつく箇所はK個じゃなくてK-1個なので注意

    runs = []
    cnt = 1
    for i in range(1, len(S)):
        if S[i] == S[i-1]:
            cnt += 1
        else:
            runs.append(cnt)
            cnt = 1
    runs.append(cnt)

    if len(runs) == 1:
        print(len(S)*K//2)
        return

    head = runs[0]
    tail = runs[-1]

    middle = 0
    for l in runs[1:-1]:
        middle += l//2

    if S[0] != S[-1]:
        print((head//2 + middle + tail//2) * K)
        return

    ans = middle*K + head//2 + tail//2 + (head+tail)//2 * (K-1)
    print(ans)
    return

main()
