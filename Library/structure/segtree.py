"""セグメント木: 配列の 1 点更新と区間 [L, R) の集計 (min, sum など) をどちらも O(log N) で行う。

    st = SegTree([5, 3, 7, 1], mode='min')
    st.query(0, 3)     ->  3     # A[0], A[1], A[2] の最小値。R は含まない
    st.update(1, 10)            # A[1] = 10 (st[1] = 10 とも書ける)
    st.query(0, 3)     ->  5
    st[2]              ->  7

    SegTree(A, mode='sum')                                # 区間和
    SegTree(A, func=lambda a, b: a + b, default=0)        # 自作の演算

使い分け:
    - 値が変わらないなら累積和 (itertools.accumulate) の方が簡単で速い
    - 区間に一括で足す / 代入する (区間更新) はこの実装ではできない (遅延セグ木が必要)

mode で選べる演算と単位元 (default):
    min (10^18 程度の大きな数), max (その負), sum (0), prd = 積 (1), gcd (0),
    lmc = 最小公倍数 lcm のつづり違い (1), ^ = XOR (0), & = AND (全ビット 1), | = OR (0)
    単位元 = 「その値と演算しても相手が変わらない値」。min なら無限大、sum なら 0。
    自作の演算 func を渡すときは、結合法則 (a*b)*c == a*(b*c) が成り立ち、
    その単位元を default に渡すこと。

仕組み:
    要素数を 2 の累乗 N2 に切り上げた完全二分木を配列 dat で持つ。
    葉 dat[N2 + i] が A[i]、内部ノード dat[j] は 2 つの子 dat[2j], dat[2j+1] の集計結果。
    - update : 葉を書き換え、親へ i >>= 1 で上りながら集計し直す (高さ分 = O(log N))
    - query  : 左端 L と右端 R から同時に上り、区間からはみ出さないノードだけを集めていく。
               左右で別々に集めて最後に合わせるので、非可換な演算でも順番が崩れない。

計算量: 構築 O(N)、update / query は O(log N)。
"""
#https://qiita.com/tomato1997/items/da9a7a73f2301aa48896

import math

class SegTree:
    DEFAULT = {
        'min': 1 << 60,
        'max': -(1 << 60),
        'sum': 0,
        'prd': 1,
        'gcd': 0,
        'lmc': 1,
        '^': 0,
        '&': (1 << 60) - 1,
        '|': 0,
    }

    FUNC = {
        'min': min,
        'max': max,
        'sum': (lambda x, y: x + y),
        'prd': (lambda x, y: x * y),
        'gcd': math.gcd,
        'lmc': (lambda x, y: (x * y) // math.gcd(x, y)),
        '^': (lambda x, y: x ^ y),
        '&': (lambda x, y: x & y),
        '|': (lambda x, y: x | y),
    }

    def __init__(self, ls, mode='min', func=None, default=None):
        """
        要素ls, 関数mode (min,max,sum,prd(product),gcd,lmc,^,&,|)
        func,defaultを指定すれば任意の関数、単位元での計算が可能
        """
        N = len(ls)
        if default == None:
            self.default = self.DEFAULT[mode]
        else:
            self.default = default
        if func == None:
            self.func = self.FUNC[mode]
        else:
            self.func = func
        self.N = N
        # 葉の数 N2 = N 以上の最小の 2 の累乗
        self.K = (N - 1).bit_length()
        self.N2 = 1 << self.K
        self.dat = [self.default] * (2**(self.K + 1))
        for i in range(self.N):  # 葉の構築
            self.dat[self.N2 + i] = ls[i]
        self.build()

    def build(self):
        # 下の段から順に、子 2 つの集計で親を埋める
        for j in range(self.N2 - 1, -1, -1):
            self.dat[j] = self.func(self.dat[j << 1], self.dat[j << 1 | 1])  # 親が持つ条件

    def leafvalue(self, x):  # リストのx番目の値
        return self.dat[x + self.N2]

    def update(self, x, y):  # index(x)をyに変更
        i = x + self.N2
        self.dat[i] = y
        while i > 0:  # 親の値を変更
            i >>= 1
            self.dat[i] = self.func(self.dat[i << 1], self.dat[i << 1 | 1])
        return

    def query(self, L, R):  # [L,R)の区間取得
        L += self.N2
        R += self.N2
        # vL: 左から集めた分、vR: 右から集めた分
        vL = self.default
        vR = self.default
        while L < R:
            # L が右の子なら、親に上がると区間外を含むので、そのノードだけ取って右へずらす
            if L & 1:
                vL = self.func(vL, self.dat[L])
                L += 1
            # R (含まない) が右の子なら、その左隣のノードを取る
            if R & 1:
                R -= 1
                vR = self.func(self.dat[R], vR)
            L >>= 1
            R >>= 1
        return self.func(vL, vR)

    def __iter__(self):
        for i in range(self.N):
            yield self[i]

    # st[i] で値の取得、st[i] = v で update
    def __getitem__(self, x): return self.leafvalue(x)
    def __setitem__(self, x, val): return self.update(x, val)
