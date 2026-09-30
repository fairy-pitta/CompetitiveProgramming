
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

def main():
    H, W = inmap()
    field = []
    for _ in range(H):
        s = list(input())
        field.append(s)

    uf = UnionFind(H*W)
    for row in range(H):
        for col in range(W):
            if field[row][col] == '#':
                num = row * W + col 
                if 0 < row:
                    # check top 
                    if field[row-1][col] == "#":
                        if not uf.is_same(num, num-W):
                            uf.unite(num, num-W)
                if 0 <= col-1: 
                    # check left 
                    if field[row][col-1] == "#":
                        if not uf.is_same(num, num-1):
                            uf.unite(num, num-1)
                if col + 1 < W:
                    # check right 
                    if field[row][col+1] == "#":
                        if not uf.is_same(num, num+1):
                            uf.unite(num, num+1)
                if row+1 < H:
                    # check bottom 
                    if field[row+1][col] == "#":
                        if not uf.is_same(num, num+W):
                            uf.unite(num, num+W)
    
    ans = 0
    for li in uf.groups():
        one = li[0]
        r = one // W
        c = one % W
        if field[r][c] == "#":
            ans += 1 
    
    return ans 

print(main())