"""優先度付きキュー: 入れた値のうち一番小さいものを O(log N) で取り出せる箱。

    pq = PriorityQueue()
    pq.push(5); pq.push(1); pq.push(3)
    pq.pop()   ->  1
    len(pq)    ->  2
    while pq: ...          # 空になるまで回せる

中身は標準の heapq そのもので、heapq.heappush(list, x) を pq.push(x) と書けるようにしただけ。
速さが気になるなら heapq を直接使っても同じ。

使い方のコツ:
    - 最大値を取り出したいときは符号を反転して入れる: push(-x)、取り出したら -pop()
    - タプルを入れると 1 要素目で比較される: push((距離, 頂点)) がダイクストラの定番
    - 一番小さい値を消さずに見たいときは pq._container[0]

計算量: push / pop は O(log N)、len は O(1)。
任意の値の削除や「x 以上で最小」の検索はできないので、必要なら sorted_set.py / multiset.py を使う。
"""

import heapq

class PriorityQueue:
    def __init__(self):
        self._container = []

    def push(self, x):
        heapq.heappush(self._container, x)

    def pop(self):
        return heapq.heappop(self._container)

    def __len__(self):
        return len(self._container)