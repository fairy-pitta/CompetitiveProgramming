# ライブラリさんたち
from collections import deque, Counter, defaultdict
from operator import itemgetter 
from bisect import bisect_right, bisect_left 
from itertools import combinations, permutations, accumulate, product
import heapq
# from numpy import base_repr
from copy import deepcopy
import sys
# sys.setrecursionlimit(10**6)
from math import gcd, log2, log10

# 便利な関数くん
def my_lcm(a, b):
    return a * b // gcd(a, b)
def my_ceil(N, W):
    return (-(-N//W))
def out(func):
    if func: print("Yes")
    else: print("No")
def inint(): return int(input())
def inmap(): return map(int, input().split())
def inlist(): return list(input())
def ingraph(N): return [[] for _ in range(N)]
def indist(N): return [(-1) for _ in range(N)]
def inseen(N): return [(False) for _ in range(N)]

# 定数ちゃん
# MOD = 998244353
# MOD = 1000000007
# INF = 10 ** 18 + 1


from typing import List

class UnionFind:
    """0-indexed"""

    def __init__(self, n):
        self.n = n
        self.parent = [-1] * n
        self.__group_count = n

    def unite(self, x, y) -> bool:
        """xとyをマージ"""
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return False

        self.__group_count -= 1

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
        """連結成分の数を取得 O(1)"""
        return self.__group_count


# N = 10
# uf = UnionFind(N)

# # connect path 
# uf.unite(1,2)
# uf.unite(2,3)
# uf.unite(5,6)
# uf.unite(7,9)
# uf.unite(9,8)
# uf.unite(5,3)

# judge if two edges are connected 
# print("is 2 and 6 in the same tree?:", uf.is_same(2,6))
# True

# find the root 
# print("the root of 5 is:", uf.root(5))
# 1

# how many edges are in the tree? 
# print("3 belongs to a tree of the size:", uf.size(3))
# 5

# print("all sizes:", uf.all_sizes())
# all sizes: [1, 5, 1, 3]

# print("all groups:", uf.groups())
# all groups: [[0], [1, 2, 3, 5, 6], [4], [7, 8, 9]] 

# how many trees?
# print(len(uf.all_sizes()))
# 4

def main():
    H, W = inmap()
    Q = inint()
    field = [inseen(W) for _ in range(H)]
    uf = UnionFind(H * W)
    direc = [()]
    for i in range(Q):
        s = list(inmap())
        t = s[0]
        if t == 1:
            row = s[1] - 1
            col = s[2] - 1
            num = W * row + col
            field[row][col] = True 
            # up 
            if row > 0:
                if field[row-1][col]:
                    uf.unite(num, num-W)
            # left 
            if col > 0:
                if field[row][col-1]:
                    uf.unite(num, num-1)
            # bottom
            if row < H-1:
                if field[row+1][col]:
                    uf.unite(num, num+W)
            # left
            if col < W-1:
                if field[row][col+1]:
                    uf.unite(num, num+1)
        else:
            Ar = s[1] - 1 
            Ac = s[2] - 1 
            Br = s[3] - 1 
            Bc = s[4] - 1 
            Anum = W * Ar + Ac
            Bnum = W * Br + Bc
            if field[Ar][Ac] and field[Br][Bc] and uf.is_same(Anum, Bnum):
                print("Yes")
            else:
                print("No")

main()