# numpy が使える環境なら base_repr が早い
# digits = base_repr(int, base)
# int = int(digits, base)
# 2 <= base <= 36


# base進法を10進法に変換する
def N_to_Dec(digits, base):
    num = 0
    digits = [int(a) for a in str(digits)]
    for digit in digits:
        num = num * base + digit
    return num


# 10進法をn進法に変換する
def base10to(n, b):
    if n // b:
        return base10to(n // b, b) + str(n % b)
    return str(n % b)