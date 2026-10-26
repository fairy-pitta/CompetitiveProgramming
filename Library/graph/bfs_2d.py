"""グリッド BFS (ABC276E 専用): S を通る長さ 4 以上の閉路があるかを判定する。

汎用のグリッド最短距離ではなく、ABC276E「Round Trip」を解いたときの関数をそのまま置いている。
https://atcoder.jp/contests/abc276/tasks/abc276_e

呼び出し方 (Daily_Practice/2023.12/2023.12.27/ABC276E.py):
    S の上下左右のうち "." のマス (y, x) それぞれについて
        bfs(y, x, H, W, C, sx, sy)
    を呼び、どれか 1 つでも "Yes" なら答えは Yes。

引数:
    y, x   : BFS の出発マス (S の隣のマス)。行 y, 列 x の順
    H, W   : グリッドの行数・列数
    Graph  : グリッド (文字列のリスト)。"#" は壁
    sx, sy : S の位置。こちらは列 sx, 行 sy の順なので注意
戻り値: "Yes" か "No" の文字列

仕組み:
    S の隣から BFS し、S に戻ってこられたら閉路がある。dist は S から数えた歩数で、
    出発マスが 1。戻るときに dist + 1 < 4 (= 隣からすぐ S に戻るだけ) の場合は除外する。

汎用のグリッド BFS (最短距離) にしたいときのひな形:
    dist = [[-1] * W for _ in range(H)]; dist[sy][sx] = 0; q = deque([(sy, sx)])
    while q: 取り出して上下左右を見て、範囲内・壁でない・dist == -1 なら dist を +1 して積む

計算量: O(HW) を出発マスの数 (最大 4) 回。
"""
from collections import deque

def bfs(y, x, H, W, Graph, sx, sy):
    seen = [[False] * W for _ in range(H)]
    seen[y][x] = True
    queue = deque([(y, x, 1)])

    while queue:
        r, c, dist = queue.popleft()
        # 左・右・上・下
        next_xy = [(r, c-1), (r, c+1), (r-1, c), (r+1, c)]
        for ny, nx in next_xy:
            # グリッドの外
            if not (0 <= ny < H and 0 <= nx < W):
                continue
            # 訪問済み / S にすぐ戻るだけ / 壁 はスキップ
            if seen[ny][nx] or ((nx, ny) == (sx, sy) and dist + 1 < 4) or Graph[ny][nx] == "#":
                continue
            if (nx, ny) == (sx, sy):
                return "Yes"

            queue.append((ny, nx, dist + 1))
            seen[ny][nx] = True

    return "No"