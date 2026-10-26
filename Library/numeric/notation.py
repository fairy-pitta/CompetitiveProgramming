"""進数変換: 10 進数と b 進数 (2 <= b <= 10) の相互変換。

    N_to_Dec(1011, 2)  ->  11      # 2 進数の 1011 を 10 進数へ
    base10to(11, 2)    ->  "1011"  # 10 進数の 11 を 2 進数の文字列へ

注意:
    - どちらも各桁を 0〜9 の 1 文字で表すので、11 進数以上 (A, B, ... を使う) には使えない。
      16 進数などは標準の int("ff", 16) や format(255, "x") を使う。
    - base10to は n >= 0 が前提。
"""

# numpy が使える環境なら base_repr が早い
# digits = base_repr(int, base)
# int = int(digits, base)
# 2 <= base <= 36


# base進法を10進法に変換する
def N_to_Dec(digits, base):
    """digits (int でも str でもよい) を base 進数として読み、10 進数の int を返す。"""
    num = 0
    digits = [int(a) for a in str(digits)]
    # 上の桁から順に「これまでの値 * base + 今の桁」
    for digit in digits:
        num = num * base + digit
    return num


# 10進法をn進法に変換する
def base10to(n, b):
    """n を b 進数で表した文字列を返す。n // b を再帰で変換し、最後に n % b の桁を付ける。"""
    if n // b:
        return base10to(n // b, b) + str(n % b)
    return str(n % b)