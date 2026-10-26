"""グラフの入力の受け取り方のスニペット集 (関数ではない)。

ファイル全体を貼ると input() が何度も走るので、必要なブロックだけをコピーして使う。
どのブロックも入力の頂点番号 1〜N を 0〜N-1 に直して格納する。

    隣接リスト         : graph[a] = [b, c, ...]          メモリ O(N + M)。ほとんどの問題はこれ
    隣接リスト (重み)  : graph[a] = [[b, w], ...]        dijkstra.py に渡す形
    隣接行列           : graph[a][b] = 1 (辺あり) / 0    メモリ O(N^2)。N <= 1000 程度まで
    隣接行列 (重み)    : graph[a][b] = w                 ワーシャルフロイドなど
    リスト <-> 行列の変換

有向グラフ (a -> b の一方通行) なら「remove if directional」の行を消す。
"""
# Adjacency list

# 各ノードから辺が存在するノードを
# リストをして各ノードに保持する

# N: nodes
# M: edges
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a,b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1) # remove if directional
# [[2,3,5], ..., [1,3,4]]

# with weight on edges
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a,b,w = map(int, input().split())
    graph[a-1].append([b-1, w])
    graph[b-1].append([a-1, w]) # remove if directional



# Adjacency matrix

# 各ノードからそれぞれのノードにおいて
# 辺が存在していれば１
# 辺が存在しなければ０
# 二次元配列に持つ、サイズはN*N

N, M = map(int, input().split())
graph = [[0] * N for _ in range(N)]
for _ in range(M):
    a,b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1 # remove if directional

N, M = map(int, input().split())
graph = [[0] * N for _ in range(N)]
for _ in range(M):
    a,b, w = map(int, input().split())
    graph[a-1][b-1] = w
    graph[b-1][a-1] = w # remove if directional


# Adjacency list to matrix
# (重みなしの隣接リストを前提とする)
graph_new = [[0] * N for _ in range(N)]
for i, g_i in enumerate(graph):
    for j in g_i:
        graph_new[i][j] = 1

# Adjacency matrix to list
# (値が 0 より大きいマスを辺とみなす)
graph_new = []
for i in range(N):
    tmp_l = []
    for  j in range(N):
        if graph[i][j] > 0:
            tmp_l.append(j)
    graph_new.append(tmp_l)


