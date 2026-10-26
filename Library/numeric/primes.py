"""エラトステネスの篩: 0 〜 N の各数が素数かどうかをまとめて求める。

    Eratosthenes(10)  ->  [F, F, T, T, F, T, F, T, F, F, F]   # isprime[i] で i が素数か
    primes_list(10)   ->  [2, 3, 5, 7]

使い分け:
    - Eratosthenes : 「x は素数か」を何度も O(1) で聞きたいとき
    - primes_list  : 素数そのものを列挙したいとき
    - 1 つの数だけ素数か調べたい / 分解したいなら factorize.py (O(√N)) の方が軽い

仕組み:
    2 から順に見て、まだ素数として残っている p の倍数 2p, 3p, ... をすべて「素数でない」に塗る。
    最後まで塗られなかった数が素数。

計算量: O(N log log N)。メモリ O(N) なので N は 10^7 程度まで。
"""

# judge if i is prime for all integer i between 1 and N
# returns a boolean list of [0, N+1] with prime number being True

def Eratosthenes(N: int) -> list:
    """長さ N+1 のリストを返す。isprime[i] が True なら i は素数。N >= 1 が前提。"""
    isprime = [True] * (N+1)
    # 0 and 1 are not prime numbers
    isprime[0], isprime[1] = False, False

    for p in range(2, N+1):
        # if its already a composite number, skip
        if not isprime[p]: continue

        # p 自身は残し、2p, 3p, ... を消す
        q = p * 2
        while q <= N:
            isprime[q] = False
            q += p

    return isprime

# 1 から N までの素数を列挙して返す
# 真偽リストではなく素数そのものが欲しいときに使う

def primes_list(N: int) -> list:
    """N 以下の素数を小さい順に返す。"""
    isprime = Eratosthenes(N)
    return [i for i in range(N + 1) if isprime[i]]
