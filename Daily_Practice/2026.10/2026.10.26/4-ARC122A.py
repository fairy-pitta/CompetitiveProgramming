# ARC122A  茶 (diff 783 / 200pt)
# https://atcoder.jp/contests/arc122/tasks/arc122_a

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
MOD = 1000000007
# INF = 10 ** 18 + 1


def main():
    N = int(input())
    A = list(map(int, input().split()))
    #dp[[合計、場合のかず]][[合計、場合の数]] ... i個の数を見たときに、最後の演算子が+の合計
    
    dp = [[[0,0],[0,0]] for i in range(N+2)]
    dp[0][0] = [A[0],1]

    for i in range(N-1):
        # +の場合の数は手前の+と-を合算する
        dp[i+1][0][1] = dp[i][0][1] + dp[i][1][1]
        # -の場合の数は手前の+のみ
        dp[i+1][1][1] = dp[i][0][1]

        # + の合計は、手前の+の合計 x A[i+1] + 手前の-の合計 x A[i+1] 場合の数分足す感じ
        dp[i+1][0][0] = (dp[i][0][0] + dp[i][1][0] + A[i+1] * dp[i][0][1] + A[i+1] * dp[i][1][1]) % MOD 

        # -の合計は、手前の+の合計 x A[i+1] を引く
        dp[i+1][1][0] = (dp[i][0][0] - A[i+1]*dp[i][0][1]) % MOD

    print((dp[N-1][0][0]+dp[N-1][1][0]) % MOD)
    return
main()



