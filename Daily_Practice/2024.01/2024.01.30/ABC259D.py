N = int(input())
sx, sy, tx, ty = map(int, input().split())

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


def is_connected(x1, y1, r1, x2, y2, r2):
    dist = abs(x1-x2)**2 + abs(y1-y2)**2

    if abs(r1-r2)**2 <= dist <= abs(r1+r2)**2:
        return True
    return False    

def is_on_circle(x, y, x1, y1, r):
    if (x1-x)**2 + (y1-y)**2 == r**2:
        return True
    return False 

uf = UnionFind(N)
circles = []

start_circle = -1
goal_circle = -1

for i in range(N):
    x, y, r = map(int, input().split())

    if is_on_circle(sx, sy, x, y, r):
        start_circle = i
    if is_on_circle(tx, ty, x, y, r):
        goal_circle = i
    
    for cx, cy, cr, num in circles:
        if is_connected(x,y,r,cx,cy,cr):
            uf.unite(i, num)
    
    circles.append((x, y, r, i))

# print(uf.groups())

if uf.is_same(start_circle, goal_circle):
    print("Yes")
else:
    print("No")