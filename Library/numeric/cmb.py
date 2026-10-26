"""二項係数 nCr: n 個から r 個を選ぶ組み合わせの数を、多倍長整数でそのまま計算する。

    cmb(5, 2)  ->  10
    cmb(4, 4)  ->  1

仕組み: nCr = n(n-1)...(n-r+1) / r!。nCr = nC(n-r) なので小さい方の r で計算して掛け算を減らす。

計算量: O(r) 回の掛け算。ただし値そのものが巨大になるので、n が大きい (10^5 など) か
何度も呼ぶ場合は遅い。「998244353 で割った余り」を求める問題では、階乗とその逆元を
前計算する方式（modint.py の割り算を使うなど）にすること。

注意: n <= 1 のときは r に関係なく 0 を返す（cmb(1, 1) や cmb(1, 0) も 0）。
      数学的には 1 なので、n が 1 以下になりうる問題では使う前に場合分けすること。
      r > n のときの挙動も保証していない。
"""
from operator import mul
from functools import reduce

def cmb(n,r):
    if n <= 1: return 0
    r = min(n-r,r)
    if r == 0: return 1
    # 分子 n * (n-1) * ... * (n-r+1)
    nume = reduce(mul, range(n, n - r, -1))
    # 分母 r!
    denom = reduce(mul, range(1, r + 1))
    return nume // denom