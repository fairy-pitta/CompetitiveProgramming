"""素因数分解: N を素数の累乗の積に分け、[[素数, 指数], ...] を素数の小さい順に返す。

    factorize(12)   ->  [[2, 2], [3, 1]]      # 12  = 2^2 * 3^1
    factorize(360)  ->  [[2, 3], [3, 2], [5, 1]]
    factorize(13)   ->  [[13, 1]]             # 素数なら自分自身だけ
    factorize(1)    ->  []

divisors.py との違い:
    - factorize     : 素数と指数がほしいとき（約数の個数 = (e1+1)(e2+1)...、
                      平方数判定 = 指数がすべて偶数、gcd/lcm を指数で考える、など）
    - calc_divisors : 約数そのものを全部並べてほしいとき

仕組み:
    p = 2, 3, 4, ... で割れるだけ割り、割れた回数 e を記録する。小さい素数で割り切ってから
    進むので、合成数 (4, 6, ...) で割れることはもう無く、記録されるのは素数だけになる。
    p * p > N になったら打ち切る。そのとき N に残っている数が 1 でなければ、
    それは √(元の N) より大きい素数がちょうど 1 つ残ったもの。

計算量: O(√N)。
前提: N >= 1 の整数。
"""


# [[factor, time]]
def factorize(N) -> list:
    ans = []

    for p in range(2, N):
        # while p * p <= N
        if p * p > N:
            break

        # if N cannot be divided by p
        # skip p
        if N % p != 0:
            continue

        # power
        e = 0
        while N % p == 0:
            e += 1
            N //= p

        ans.append([p, e])

    # 残った N は √N より大きい素数 (例: 26 = 2 * 13 の 13)
    if N != 1:
        ans.append([N, 1])

    return ans