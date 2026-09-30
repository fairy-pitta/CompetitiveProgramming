# 二部グラフ判定
from collections import deque


def b_judge(now, graph, color, stack):
    while len(stack) > 0:
        now = stack.popleft()
        for v2 in graph[now]:
            if color[v2] != -1:
                if color[v2] == color[now]:
                    return False 
                else:
                    continue 
            color[v2] = 1 - color[now]
            stack.append(v2)
    
    return True


def is_bipartite(N, graph) -> bool:
    """連結でないグラフも含めて二部グラフか判定する"""
    color = [-1] * N
    for start in range(N):
        if color[start] != -1:
            continue
        color[start] = 1
        stack = deque([start])
        if not b_judge(start, graph, color, stack):
            return False
    return True
