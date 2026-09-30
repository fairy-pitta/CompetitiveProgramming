
def main():
    N, K, S = map(int, input().split())

    if S == 10**9:
        ans = [(10**9) for _ in range(K)] + [(1) for _ in range(N-K)]
    else:
        ans = [(S) for _ in range(K)] + [(10**9) for _ in range(N-K)]
    
    print(*ans)

main()