# A, B の最大公約数を返す関数
def GCD(A, B):
    if B == 0:
        return A
    else:
        return GCD(B, A % B)

def main():
    A, B, C = map(int, input().split())
    g = GCD(A, B)
    if C%g == 0:
        print("YES")
    else:
        print("NO")

main()


