"""約数列挙: N を割り切る数をすべて小さい順に返す。

    calc_divisors(12)  ->  [1, 2, 3, 4, 6, 12]

factorize.py との違い:
    - calc_divisors : 「N を割り切る数」を全部ほしいとき（約数の個数・総和、約数ごとの全探索など）
    - factorize     : 「N = p1^e1 * p2^e2 * ...」の素数と指数がほしいとき
    12 なら calc_divisors は [1, 2, 3, 4, 6, 12]、factorize は [[2, 2], [3, 1]]（12 = 2^2 * 3^1）。

仕組み:
    i が N の約数なら N // i も約数になる。i と N // i の小さい方は必ず √N 以下なので、
    i を 1 から √N まで試し、見つかるたびに i と N // i をペアで追加すれば全部そろう。
    i * i == N のときは同じ数を 2 回入れないよう 1 回だけ追加する。

計算量: O(√N)。N = 10^12 でも 10^6 回程度のループで終わる。
前提: N >= 1 の整数。
"""


def calc_divisors(N) -> list:
    res = []

    for i in range(1, N+1):
        # i が √N を超えたら、残りの約数はすべて N // i として追加済み
        if i * i > N:
            break

        if N % i != 0:
            continue

        res.append(i)

        # ペアの相方。i * i == N のときは同じ数なので入れない
        if N // i != i:
            res.append(N // i)

    # 追加順は 1, N, 2, N/2, ... とバラバラなので最後に並べる
    res.sort()

    return res