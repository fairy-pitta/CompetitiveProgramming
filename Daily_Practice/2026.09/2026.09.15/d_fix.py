from typing import List

class UnionFind:
    """0-indexed"""

    def __init__(self, n):
        self.n = n
        self.parent = [-1] * n
        self.__group_count = n
        # 連結成分ごとの黒の数（root(x) の位置の値だけが有効）
        self.__black_count = [0] * n

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

        # 吸収したyの黒の数を新しい根xに合算
        self.__black_count[x] += self.__black_count[y]
        self.__black_count[y] = 0

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


    def add_black(self, x):
        self.__black_count[self.root(x)] += 1

    def remove_black(self, x):
        self.__black_count[self.root(x)] -= 1

    def is_connected(self, x):
        if self.__black_count[self.root(x)] >= 1:
            return True

        return False



    @property
    def group_count(self) -> int:
        """連結成分の数を取得 O(1)"""
        return self.__group_count


N, Q = map(int, input().split())
uf = UnionFind(N+1)
point_list = ["White" for _ in range(N)]

for _ in range(Q):
    order = list(map(int, input().split()))
    if order[0] == 1:
        uf.unite(order[1], order[2])
    elif order[0] == 2:
        if point_list[order[1]-1] == "White":
            point_list[order[1]-1] = "Black"
            uf.add_black(order[1])
        else:
            point_list[order[1]-1] = "White"
            uf.remove_black(order[1])

    else:
        if uf.is_connected(order[1]):
            print("Yes")
        else:
            print("No")
