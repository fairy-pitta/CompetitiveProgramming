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
        self.K = (N - 1).bit_length()
        self.N2 = 1 << self.K
        self.dat = [self.default] * (2**(self.K + 1))
        for i in range(self.N):  # 葉の構築
            self.dat[self.N2 + i] = ls[i]
        self.build()

    def build(self):
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
        vL = self.default
        vR = self.default
        while L < R:
            if L & 1:
                vL = self.func(vL, self.dat[L])
                L += 1
            if R & 1:
                R -= 1
                vR = self.func(self.dat[R], vR)
            L >>= 1
            R >>= 1
        return self.func(vL, vR)

    def __iter__(self):
        for i in range(self.N):
            yield self[i]

    def __getitem__(self, x): return self.leafvalue(x)
    def __setitem__(self, x, val): return self.update(x, val)


N, Q = map(int, input().split())
S = list(input())

seq = []
for i in S:
    if i == "(":
        seq.append(1)
    else:
        seq.append(-1)

acc_seq = []
for j in range(N):
    if j == 0:
        acc_seq.append(seq[j])
    else:
        acc_seq.append(acc_seq[-1]+seq[j])


sum_segtree = SegTree(seq, mode="sum")
min_segtree = SegTree(acc_seq, mode="sum")

for _ in range(Q):
    t, l, r = map(int, input().split())
    if t == 1:
        l -= 1
        r -= 1 
        v1, v2 = sum_segtree.leafvalue(l), sum_segtree.leafvalue(r)
        v3, v4 = min_segtree.leafvalue(l), min_segtree.leafvalue(r)

        sum_segtree.update(l, v2)
        sum_segtree.update(r, v1)
        min_segtree.update(l, v4)
        min_segtree.update(r, v3)
    
    else:
        l -= 1
        s = sum_segtree.query(l, r)
        m = min_segtree.query(l, r)

        print(s, m)
        if s == 0 and m == 0:
            print("Yes")
        else:
            print("No")
