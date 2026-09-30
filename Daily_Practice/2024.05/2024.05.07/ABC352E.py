from typing import List

class UnionFind:
    """A class for Union-Find data structure (Disjoint Set Union, DSU)"""

    def __init__(self, n: int):
        self.n = n
        self.parent = [-1] * n
        self.__group_count = n

    def unite(self, x: int, y: int) -> bool:
        """Union x and y; returns False if they are already connected."""
        x_root = self.root(x)
        y_root = self.root(y)

        if x_root == y_root:
            return False

        self.__group_count -= 1

        if self.parent[x_root] > self.parent[y_root]:
            x_root, y_root = y_root, x_root

        self.parent[x_root] += self.parent[y_root]
        self.parent[y_root] = x_root
        return True

    def is_same(self, x: int, y: int) -> bool:
        """Check if x and y are in the same group."""
        return self.root(x) == self.root(y)

    def root(self, x: int) -> int:
        """Find the root of x with path compression."""
        if self.parent[x] < 0:
            return x
        self.parent[x] = self.root(self.parent[x])
        return self.parent[x]

    def size(self, x: int) -> int:
        """Return the size of the group to which x belongs."""
        return -self.parent[self.root(x)]

    def all_sizes(self) -> List[int]:
        """Return the sizes of all groups in the Union-Find."""
        return [-self.parent[i] for i in range(self.n) if self.parent[i] < 0]

    def groups(self) -> List[List[int]]:
        """Return a list of all groups."""
        root_to_group = {}
        for i in range(self.n):
            root = self.root(i)
            if root not in root_to_group:
                root_to_group[root] = []
            root_to_group[root].append(i)
        return list(root_to_group.values())

    @property
    def group_count(self) -> int:
        """Return the number of distinct groups."""
        return self.__group_count

# Reading input
N, M = map(int, input().split())
uf = UnionFind(N)

connections = []
for _ in range(M):
    K, C = map(int, input().split())
    A = list(map(lambda x: int(x) - 1, input().split()))
    connections.append((C, K, A))

# Sorting by cost to implement a kind of Kruskal's algorithm
connections.sort()

total_cost = 0
for cost, _, nodes in connections:
    base_node = nodes[0]
    for node in nodes[1:]:
        if not uf.is_same(base_node, node):
            if uf.unite(base_node, node):
                total_cost += cost

# Check if all nodes are connected
if uf.group_count > 1:
    print(-1)
else:
    print(total_cost)
