"""めぐる式二分探索: 「条件を満たす / 満たさない」の境目を O(log(r - l)) 回の判定で探す。

使い方:
    1. 先に check(x) を定義する (この関数はグローバルの check を呼ぶ)。
       check は単調でなければならない: ある値を境に False...False True...True (またはその逆) になる。
    2. 引数は「絶対に条件を満たさない値 ng」と「必ず条件を満たす値 ok」。
       meguru_bisect(ng, ok) の順に渡す。
    3. 戻り値は境目にある ok 側の値。

    # 例: x * x >= 50 となる最小の x
    def check(x): return x * x >= 50
    meguru_bisect(0, 50)   ->  8          # 0 は満たさない、50 は満たす

    # 例: 条件を満たす最大の値を探すときは ng と ok の大小が逆になるだけ
    def check(x): return x * x <= 50
    meguru_bisect(51, 0)   ->  7

ng / ok の初期値の決め方:
    ng = (とり得る最小値) - 1、ok = (とり得る最大値) + 1 のように、答えの範囲の「外側」にとる。
    こうすると check を一度も呼ばずに済む端の値を気にしなくてよい。

仕組み:
    l (ng) と r (ok) の真ん中 mid を check し、満たすなら ok 側 (r) を、
    満たさないなら ng 側 (l) を mid に縮める。差が 1 になったら r が境目の ok。
    abs をとっているので l < r でも l > r でも同じコードで動く。

注意: 引数名は l, r だが意味は「l = ng、r = ok」。左右ではない。
計算量: check の呼び出しが O(log |r - l|) 回。
"""
def meguru_bisect(l, r):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    l r は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(r - l) > 1):
        mid = (r + l) // 2
        if check(mid):
            r = mid
        else:
            l = mid
    return r
