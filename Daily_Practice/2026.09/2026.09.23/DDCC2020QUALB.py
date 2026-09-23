# DDCC2020QUALB  灰 (diff 350 / 100pt)
# https://atcoder.jp/contests/ddcc2020/tasks/ddcc2020_qual_b




## frequently used functions 
from collections import deque, Counter, defaultdict
from operator import itemgetter 
from bisect import bisect_right, bisect_left, insort
from itertools import combinations, permutations, accumulate, product, groupby
import heapq
# from numpy import base_repr
from copy import deepcopy
import sys
# sys.setrecursionlimit(10**9)
from math import gcd, log2, log10
from functools import lru_cache, reduce 


def main():
    data = sys.stdin.buffer.read().split()
    Q = int(data[0])

    # クエリを先読みして、登場する値を座標圧縮する
    queries = []
    xs = []
    p = 1
    for _ in range(Q):
        t = int(data[p])
        if t == 1:
            x = int(data[p+1])
            queries.append((1, x, 0))
            p += 2
        else:
            x = int(data[p+1])
            k = int(data[p+2])
            queries.append((t, x, k))
            p += 3
        xs.append(x)

    xs = sorted(set(xs))
    comp = {x: i+1 for i, x in enumerate(xs)}  # 1-indexed
    N = len(xs)
    tree = [0] * (N+1)
    LOG = 1 << (N.bit_length())
    total = 0  # 今までに挿入した個数

    ans = []
    for t, x, k in queries:
        pos = comp[x]

        if t == 1:
            # 挿入
            total += 1
            while pos <= N:
                tree[pos] += 1
                pos += pos & -pos

        elif t == 2:
            # x 以下の数のうち大きい方から k 番目
            cnt = 0  # x 以下の個数
            i = pos
            while i > 0:
                cnt += tree[i]
                i -= i & -i
            if cnt < k:
                ans.append(-1)
            else:
                ans.append(xs[kth(tree, N, LOG, cnt-k+1) - 1])

        else:
            # x 以上の数のうち小さい方から k 番目
            cnt = 0  # x 未満の個数
            i = pos - 1
            while i > 0:
                cnt += tree[i]
                i -= i & -i
            if cnt + k > total:
                ans.append(-1)
            else:
                ans.append(xs[kth(tree, N, LOG, cnt+k) - 1])

    sys.stdout.write('\n'.join(map(str, ans)) + '\n')

    return


def kth(tree, N, LOG, k):
    """小さい方から k 番目の要素の圧縮後インデックス (1-indexed) を返す"""
    pos = 0
    step = LOG
    while step:
        nxt = pos + step
        if nxt <= N and tree[nxt] < k:
            pos = nxt
            k -= tree[pos]
        step >>= 1
    return pos + 1


main()
