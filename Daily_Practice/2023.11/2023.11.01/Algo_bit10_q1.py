
def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))

    ans = 0

    for i in range(N):
        if X & (1<<i) > 0:
            ans += A[i]
    
    print(ans)

main()