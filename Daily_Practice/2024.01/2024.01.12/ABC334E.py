from typing import List
from copy import deepcopy

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

h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
u = UnionFind(h * w)
cnt = 0
mod = 998244353
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
red = []

for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            for m in move:
                im, jm = i + m[0], j + m[1]
                if 0 <= im < h and 0 <= jm < w:
                    if s[im][jm] == "#":
                        u.unite(i * w + j, im * w + jm)
        else:
            red.append((i, j))
            
ans = 0
prev_cnt = len(u.groups()) - len(red)

for i, j in red:
    se = set()
    for m in move:
        im, jm = i + m[0], j + m[1]
        if 0 <= im < h and 0 <= jm < w:
            if s[im][jm] == "#":
                se.add(u.root(im * w + jm))
    ans += prev_cnt - len(se) + 1
    ans %= mod

ans = ans * pow(len(red), -1, mod) % mod
print(ans)

                        





