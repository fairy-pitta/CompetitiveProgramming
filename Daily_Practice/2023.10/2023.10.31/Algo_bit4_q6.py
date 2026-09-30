# Aと2**iの論理和(OR)を求める
# 整数値Aで表されるビット状態に対して、i番目のフラグを立てる操作

def main():
    A, i = map(int, input().split())
    print(A | 1<<i)

main()