from typing import List

class UnionFind:
    """0-indexed"""

    def __init__(self, n):
        self.n = n
        self.parent = [-1] * n
        self.__group_count = n
        self.__black_count = 0

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


    def add_black(self):
        self.__black_count += 1

    def remove_black(self):
        self.__black_count -= 1

    def is_connected(self):
        if self.__black_count >= 1:
            return True

        return False

    

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



N, Q = int(input().split())
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




