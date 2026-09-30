
def main():
    N = int(input())
    A = list(map(int, input().split()))

    sm = sum(A)
    ans = 10**18
    snuke = 0

    for i in range(N-1):
        snuke += A[i]
        ans = min(ans, abs(sm-2*snuke))
    
    print(ans)

main()