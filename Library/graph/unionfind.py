"""Union-Find (素集合データ構造): 「グループの合体」と「同じグループか」を高速に扱う。

    uf = UnionFind(5)        # 0〜4 がそれぞれ 1 人ずつのグループ
    uf.unite(0, 1)
    uf.unite(1, 2)
    uf.is_same(0, 2)   ->  True
    uf.size(0)         ->  3
    uf.group_count     ->  3   # {0, 1, 2}, {3}, {4}

使いどころ: 辺を足していく途中で連結かどうかを何度も聞く問題、連結成分の数・大きさ、
クラスカル法 (最小全域木)。辺の削除はできない。削除が必要なら「逆順に追加」に言い換える。

仕組み:
    各グループを木で表し、根をグループの代表にする。parent[x] は x の親で、
    x が根のときは「-(グループの大きさ)」を入れておく (負なら根、という目印も兼ねる)。
    - root      : 親をたどって根を探す。途中の頂点を根に直接つなぎ直す (経路圧縮) ので次から速い
    - unite     : 根どうしをつなぐ。小さいグループを大きいグループの下に付ける (union by size)
    この 2 つの工夫で各操作がほぼ O(1) (O(α(N))、α はアッカーマン関数の逆関数) になる。

注意: 0-indexed。入力が 1-indexed なら -1 して渡すか、UnionFind(N + 1) で作る。
"""
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




