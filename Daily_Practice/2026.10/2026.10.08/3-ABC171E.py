# ABC171E  茶 (diff 778 / 200pt)
# https://atcoder.jp/contests/abc171/tasks/abc171_e

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
    N = int(input())
    A = list(map(int, input().split()))

    # 答えを x_i、全体のXORを S = x_1^...^x_N とおくと
    # a_i は自分以外の全部のXORなので a_i = S ^ x_i  (同じ数を2回XORすると消える)
    #
    # S は答えから作る値なので直接は分からないけど、a を全部XORすると
    #   (S^x_1)^(S^x_2)^...^(S^x_N) = (Sが N個) ^ (x_1^...^x_N) = 0 ^ S = S
    # N が偶数だから S が消えてくれる。つまり a の全XORがそのまま S
    S = 0
    for a in A:
        S ^= a

    # a_i = S ^ x_i を x_i について解くと x_i = S ^ a_i
    ans = [S ^ a for a in A]

    print(*ans)
    return

main()
