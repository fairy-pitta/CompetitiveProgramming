"""ModInt: 常に MOD で割った余りを保つ整数。+ - * / ** を普通の int のように書ける。

    a = ModInt(10)
    b = a * 3 - 5        # ModInt と int を混ぜてよい
    c = 1 / a            # 割り算はモジュラ逆元 (a * c が 1 になる数) を掛ける
    print(b)             # print / str() で中身の数が出る。値そのものは b.x

使いどころ: 「答えを 998244353 で割った余りを出力せよ」で、計算途中のあちこちに
% MOD を書き忘れるのを防ぎたいとき。

仕組み:
    - 足し算・引き算・掛け算は計算後に % MOD するだけ。
    - 割り算 x / y は、MOD が素数ならフェルマーの小定理より y^(MOD-2) が y の逆元になるので、
      x * pow(y, MOD - 2, MOD) で求める。

注意:
    - MOD はグローバル変数。1000000007 を使う問題では下のコメントを切り替える。
    - 割り算は MOD が素数で、割る数が MOD の倍数でないときだけ正しい。
    - == を定義していないので ModInt(3) == 3 は False になる。比較は a.x == 3 と書く。
    - クラスなので素の int で % MOD するより数倍遅い。ループが 10^6 回を超えるなら素の int も検討。
"""
# https://qiita.com/wotsushi/items/c936838df992b706084c

MOD = 998244353
# MOD = 1000000007

class ModInt:
    def __init__(self, x):
        # 負の数も Python の % なら 0 〜 MOD-1 に収まる
        self.x = x % MOD

    def __str__(self):
        return str(self.x)

    __repr__ = __str__

    # 以下、相手 other が ModInt でも int でも動くように分岐している

    def __add__(self, other):
        return (
            ModInt(self.x + other.x) if isinstance(other, ModInt) else
            ModInt(self.x + other)
        )

    def __sub__(self, other):
        return (
            ModInt(self.x - other.x) if isinstance(other, ModInt) else
            ModInt(self.x - other)
        )

    def __mul__(self, other):
        return (
            ModInt(self.x * other.x) if isinstance(other, ModInt) else
            ModInt(self.x * other)
        )

    def __truediv__(self, other):
        # self / other = self * other^(MOD-2)
        return (
            ModInt(
                self.x * pow(other.x, MOD - 2, MOD)
            ) if isinstance(other, ModInt) else
            ModInt(self.x * pow(other, MOD - 2, MOD))
        )

    def __pow__(self, other):
        return (
            ModInt(pow(self.x, other.x, MOD)) if isinstance(other, ModInt) else
            ModInt(pow(self.x, other, MOD))
        )

    # __r**__ は 3 + a のように左側が int のときに呼ばれる
    __radd__ = __add__

    def __rsub__(self, other):
        return (
            ModInt(other.x - self.x) if isinstance(other, ModInt) else
            ModInt(other - self.x)
        )

    __rmul__ = __mul__

    def __rtruediv__(self, other):
        return (
            ModInt(
                other.x * pow(self.x, MOD - 2, MOD)
            ) if isinstance(other, ModInt) else
            ModInt(other * pow(self.x, MOD - 2, MOD))
        )

    def __rpow__(self, other):
        return (
            ModInt(pow(other.x, self.x, MOD)) if isinstance(other, ModInt) else
            ModInt(pow(other, self.x, MOD))
        )