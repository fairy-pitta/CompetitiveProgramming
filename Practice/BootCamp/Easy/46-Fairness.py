def main():
    A, B, C, K = map(int, input().split())
    if K%2:
        return (A-B)*(-1)
    else:
        return A-B

print(main())