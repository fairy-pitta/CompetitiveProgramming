def main():
    A, B = map(str, input().split())
    A = int(A)
    B_int = int(B[:-3])
    B_flo = int(B[-2:])

    float_part = A * B_flo // 100
    ans = A*B_int + float_part
    print(ans)

main()
