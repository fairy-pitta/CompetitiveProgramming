from typing import List
import heapq

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


N, M = map(int, input().split())
A = list(map(int, input().split()))
edges = [[] for _ in range(max(A)+1)]
uf = UnionFind(N)

hq = []

for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1

    if A[u] < A[v]:
        heapq.heappush(hq, (A[u], u, v))
    elif A[u] > A[v]:
        heapq.heappush(hq, (A[v], v, u))
    else:
        uf.unite(u, v)

dp = [-1] * (N)
dp[uf.root(0)] = 1

# print(uf.groups())
# print(list(hq))
# print(dp)


while len(hq) > 0:
    _, u, v = heapq.heappop(hq)
    u = uf.root(u)
    v = uf.root(v)

    if dp[u] > 0:
        dp[v] = max(dp[v], dp[u]+1)
    
    # print(dp)

print(max(0, dp[uf.root(N-1)]))




