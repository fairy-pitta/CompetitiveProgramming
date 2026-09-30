
# https://qiita.com/AkariLuminous/items/31faea745b5dd4fb9edc#2-csr%E5%BD%A2%E5%BC%8F%E3%81%AE%E5%AE%9F%E8%A3%85%E6%96%B9%E6%B3%95
# https://qiita.com/AkariLuminous/items/a2c789cebdd098dcb503#52-scc

import sys

def csr(n, E):
    start = [0] * (n + 1)
    elist = [0] * len(E)
    # start[i+1] = 頂点 i を始点とする辺の数
    for e0, e1 in E:
        start[e0 + 1] += 1
    #累積和
    for i in range(1, n + 1):
        start[i] += start[i - 1]
    #挿入位置を表すポインタ
    counter = start[:]
    for e0, e1 in E:
        elist[counter[e0]] = e1
        counter[e0] += 1 # ポインタを進める
    return start, elist


class _SCC_graph:
    def __init__(self, n):
        self._n = n
        self.edges = []
        sys.setrecursionlimit(max(2*n, sys.getrecursionlimit()))
    
    def num_vertices(self):
        return self._n
    
    def add_edge(self, frm, to):
        self.edges.append([frm, to])
    
    def scc_ids(self):
        start, elist = csr(self._n, self.edges)
        now_ord, group_num = 0, 0
        visited = []
        low = [0] * self._n
        ord_ = [-1] * self._n
        ids = [0] * self._n

        def dfs(v):
            nonlocal now_ord, group_num, visited, low, ord_, ids
            low[v] = ord_[v] = now_ord
            now_ord += 1
            visited.append(v)
            for i in range(start[v], start[v+1]):
                to = elist[i]
                if ord_[to] == -1:
                    dfs(to)
                    low[v] = min(low[v], low[to])
                else:
                    low[v] = min(low[v], ord_[to])
            if low[v] == ord_[v]:
                while True:
                    u = visited.pop()
                    ord_[u] = self._n
                    ids[u] = group_num
                    if u == v: break
                group_num += 1
        
        for i in range(self._n):
            if ord_[i] == -1: dfs(i)
        for i in range(self._n):
            ids[i] = group_num - 1 - ids[i]
        
        return group_num, ids


    def scc(self):
        group_num, ids = self.scc_ids()
        groups = [[] for _ in range(group_num)]
        for i in range(self._n):
            groups[ids[i]].append(i)
        return groups


class SCC_graph:
    def __init__(self, n):
        self._n = n
        self._scc_graph = _SCC_graph(n)
    
    def add_edge(self, frm, to):
        assert 0 <= frm < self._n
        assert 0 <= to < self._n
        self._scc_graph.add_edge(frm, to)
    
    def scc(self):
        return self._scc_graph.scc()

def build_condensed_graph(sccs, original_graph, N):
    scc_map = {}
    for i, scc in enumerate(sccs):
        for node in scc:
            scc_map[node] = i

    condensed_graph = [[] for _ in range(len(sccs))]
    for u in range(N):
        for v in original_graph[u]:
            if scc_map[u] != scc_map[v]:
                condensed_graph[scc_map[u]].append(scc_map[v])


    for i in range(len(condensed_graph)):
        condensed_graph[i] = list(set(condensed_graph[i]))

    return condensed_graph, scc_map

def calculate_reachability(condensed_graph):
    N = len(condensed_graph)
    reachability = [set() for _ in range(N)]

    def dfs(v):
        stack = [v]
        while stack:
            node = stack.pop()
            for neighbor in condensed_graph[node]:
                if neighbor not in reachability[v]:
                    reachability[v].add(neighbor)
                    stack.append(neighbor)
                    reachability[v].update(reachability[neighbor])

    for v in range(N):
        dfs(v)
        reachability[v].add(v)

    return reachability

def expand_reachability(sccs, scc_map, reachability):
    N = len(scc_map)
    expanded_reachability = [set() for _ in range(N)]
    for v in range(N):
        scc_index = scc_map[v]
        for reachable_scc in reachability[scc_index]:
            expanded_reachability[v].update(sccs[reachable_scc])
    return expanded_reachability


N = int(input())
li = list(map(int, input().split()))

graph = SCC_graph(N)
original_graph = [[] for _ in range(N)]
for i in range(N):
    graph.add_edge(i, li[i]-1)
    original_graph[i].append(li[i]-1)

sccs = graph.scc()
#print(sccs)

condensed_graph, scc_map = build_condensed_graph(sccs, original_graph, N)
#print(condensed_graph)
#print(scc_map)
reachability = calculate_reachability(condensed_graph)
#print(reachability)
expanded_reachability = expand_reachability(sccs, scc_map, reachability)

ans = 0
for i in range(N):
    ans += len(expanded_reachability[i])

print(ans)

# 10
# (1 -> 6)
# (2 -> 10)
# (3 -> 4)
# (4 -> 1)
# (5 -> 5)
# (6 -> 9)
# (7 -> 8)
# (8 -> 6)
# (9 -> 5)
# (10 -> 1)


