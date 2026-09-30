
def main():
    N = int(input())
    A = list(map(int, input().split()))
    dp = [(10**18) for _ in range(N)]
    dp[0] = 0
    dp[1] = A[0]

    for grid in range(1, N):
        dp[grid] = min(dp[grid-1]+A[grid], dp[grid-2]+2*A[grid])
    
    print(dp[-1])

main()
