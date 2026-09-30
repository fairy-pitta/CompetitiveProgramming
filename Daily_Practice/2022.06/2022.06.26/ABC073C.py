def main():
    N = int(input())
    S = set()
    for _ in range(N):
        A = int(input())
        if A not in S:
            S.add(A)
        else:
            S.discard(A)
    return len(S)

print(main())
            