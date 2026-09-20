def main():
    A,B,C = sorted(map(int, input().split()))
    if A+B<C:
        return -1
    return C

print(main())

    

    