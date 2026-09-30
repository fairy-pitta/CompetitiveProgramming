# AGC007A  茶 (diff 792 / 200pt)
# https://atcoder.jp/contests/agc007/tasks/agc007_a




## frequently used functions 
from collections import deque, Counter, defaultdict
from operator import itemgetter 
from bisect import bisect_right, bisect_left 
from itertools import combinations, permutations, accumulate, product, groupby
import heapq
# from numpy import base_repr
from copy import deepcopy
import sys
# sys.setrecursionlimit(10**9)
from math import gcd, log2, log10
from functools import lru_cache, reduce 


def main():
    H, W = map(int, input().split())
    grid = [input().strip() for _ in range(H)]

    # 右へW-1回、下へH-1回移動する全ての組み合わせを生成
    # permutationで方向の並び順を全て列挙
    moves = ['R'] * (W - 1) + ['D'] * (H - 1)

    for path_dirs in set(permutations(moves)):
        visited = set()
        r, c = 0, 0
        visited.add((0, 0))

        # パスをたどる
        for direction in path_dirs:
            if direction == 'R':
                c += 1
            else:  # 'D'
                r += 1
            visited.add((r, c))

        # チェック: 訪問したセル全てが'#'、未訪問のセル全てが'.'であるか
        valid = True
        for i in range(H):
            for j in range(W):
                if (i, j) in visited:
                    if grid[i][j] != '#':
                        valid = False
                        break
                else:
                    if grid[i][j] != '.':
                        valid = False
                        break
            if not valid:
                break

        if valid:
            print("Yes")
            return

    print("No")


main()