# ARC136A  灰 (diff 0 / 100pt)
# https://atcoder.jp/contests/arc136/tasks/arc136_a

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
    S = input()

    new_S = S.replace("A", "BB")

    #print(new_S)

    ans = ""
    idx = 0
    while True:
        if idx == len(new_S):
            break
        if idx == len(new_S) - 1:
            ans += new_S[idx]
            break
        if (new_S[idx] == "B" and new_S[idx+1] == 'B'):
            ans += "A"
            idx += 2 
            
        else:
            ans += new_S[idx]
            idx += 1

    print(ans)
        


main()