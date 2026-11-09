# ABC292D  茶 (diff 579 / 200pt)
# https://atcoder.jp/contests/abc292/tasks/abc292_d

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


from typing import List

class UnionFind:
    """0-indexed"""

    def __init__(self, n):
        self.n = n
        # 最初は全員が根で、大きさ 1 のグループ
        self.parent = [-1] * n
        self.__group_count = n

    def unite(self, x, y) -> bool:
        """xとyをマージ。もともと同じグループなら何もせず False を返す"""
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return False

        self.__group_count -= 1

        # parent は負の大きさなので、parent[x] > parent[y] は「x の方が小さい」
        # 大きい方を x にそろえる
        if self.parent[x] > self.parent[y]:
            x, y = y, x

        self.parent[x] += self.parent[y]
        self.parent[y] = x

        return True

    def is_same(self, x, y) -> bool:
        """xとyが同じ連結成分か判定"""
        return self.root(x) == self.root(y)

    def root(self, x) -> int:
        """xの根を取得"""
        if self.parent[x] < 0:
            return x
        else:
            # 経路圧縮: 根を見つけたら x の親を根に付け替える
            # 再帰なので、深くなりうる場合は sys.setrecursionlimit を上げる
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]

    def size(self, x) -> int:
        """xが属する連結成分のサイズを取得"""
        return -self.parent[self.root(x)]

    def all_sizes(self) -> List[int]:
        """全連結成分のサイズのリストを取得 O(N)
        """
        sizes = []
        for i in range(self.n):
            size = self.parent[i]
            if size < 0:
                sizes.append(-size)
        return sizes

    def groups(self) -> List[List[int]]:
        """全連結成分の内容のリストを取得 O(N・α(N))"""
        groups = dict()
        for i in range(self.n):
            p = self.root(i)
            if not groups.get(p):
                groups[p] = []
            groups[p].append(i)
        return list(groups.values())

    @property
    def group_count(self) -> int:
        """連結成分の数を取得 O(1)。() を付けずに uf.group_count と書く"""
        return self.__group_count


N, M = ismap()
uf = UnionFind(N)
edges = []
for _ in range(M):
    u, v = iszero()
    uf.unite(u, v)
    edges.append(u)

# 各連結成分の辺数を根ごとに数える
ecnt = defaultdict(int)
for u in edges:
    ecnt[uf.root(u)] += 1

ok = True
for r in range(N):
    if uf.root(r) != r:    
        continue
    if uf.size(r) != ecnt[r]:
        ok = False
out(ok)
