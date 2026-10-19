# ABC440D  緑 (diff 863 / 300pt)
# https://atcoder.jp/contests/abc440/tasks/abc440_d

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
    N, Q = map(int, input().split())
    A = sorted(list(map(int, input().split())))

    # 値が10**9まであるので使える数を並べたリストは作れない
    # なので「X以上でY番目」を「1から数えてT番目」に言い換える
    # X未満にある使える数の個数をYに足しておけば、Xのことは忘れていい

    # d[i] = A[i] - (i+1) = 1からA[i]までにある使える数の個数
    # Aはソート済みで全部違う数だからdは単調非減少、つまりにぶたんできる
    d = []
    for i in range(N):
        d.append(A[i] - (i+1))

    ans = []
    for _ in range(Q):
        X, Y = map(int, input().split())
        # bisect_leftでX未満のAの個数が出るので、X-1までの使える数の個数はこれ
        used = (X-1) - bisect_left(A, X)
        T = Y + used

        # T番目の使える数は、それより小さいAの個数kのぶん後ろにずれる
        # kはd[i] < Tになるiの個数なので、そのままbisect_left
        k = bisect_left(d, T)
        ans.append(T + k)

    print("\n".join(map(str, ans)))
    return

main()
