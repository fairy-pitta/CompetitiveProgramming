
def main():
    N, K = map(int, input().split())
    if N%K==0:
        return 0
    else:
        return min(abs(N%K-K), N%K)

print(main())