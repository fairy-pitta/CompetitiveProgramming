# A AND 2**i
# 整数値Aを二進法で表したときのi桁目に1が立っているかどうかを調べられる
def main():
    A, i = map(int, input().split())
    print(A & 1<<i)

main()
