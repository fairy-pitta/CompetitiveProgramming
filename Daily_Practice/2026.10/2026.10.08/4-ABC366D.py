# ABC366D  茶 (diff 586 / 200pt)
# https://atcoder.jp/contests/abc366/tasks/abc366_d

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

    # 3次元だけど、やることは2次元累積和の拡張
    # 各x層で(y,z)平面の2次元累積和を作って、それをx方向に足し込むだけ
    # 入力は A[x][y][z] = x層目・y行目・z列目 の順で来る

    S = [[[0] * (N+1) for _ in range(N+1)] for _ in range(N+1)]

    for x in range(1, N+1):
        for y in range(1, N+1):
            A = list(map(int, input().split()))
            acc = 0
            for z in range(1, N+1):
                acc += A[z-1]
                # acc が行方向、S[x][y-1][z] で層内の2次元累積和になる
                # さらに S[x-1][y][z] を足して、ダブった分を引けば3次元
                S[x][y][z] = acc + S[x][y-1][z] + S[x-1][y][z] - S[x-1][y-1][z]

    # クエリは包除原理、2次元の4項が3次元だと8項になる
    # 引いた添字が奇数個ならマイナス、偶数個ならプラス
    Q = int(input())
    ans = []
    for _ in range(Q):
        lx, rx, ly, ry, lz, rz = map(int, input().split())
        lx -= 1
        ly -= 1
        lz -= 1
        ans.append(S[rx][ry][rz]
                   - S[lx][ry][rz] - S[rx][ly][rz] - S[rx][ry][lz]
                   + S[lx][ly][rz] + S[lx][ry][lz] + S[rx][ly][lz]
                   - S[lx][ly][lz])

    print("\n".join(map(str, ans)))
    return

main()
