# 木の直径を求める
# 最短経路の最大値

from collections import deque
def diam(start, N, graph):
    # stack を用意、始点を追加
    stack = deque()
    stack.append(start)
    # 始点からの距離を管理
    dist = [(-1) for _ in range(N+1)]
    dist[start] = 0
    # 一番遠い点
    max_point = 0
    # 始点から一番遠い点までの距離
    max_dist = 0
    while len(stack) > 0:
        now = stack.popleft()
        togo = graph[now]
        for point in togo:
            if dist[point] != -1:
                continue 
            elif dist[now] + 1 > max_dist:
                max_point = point 
            
            stack.append(point)
            dist[point] = dist[now] + 1
            max_dist = max(max_dist, dist[now] + 1)
    
    return max_point, max_dist 