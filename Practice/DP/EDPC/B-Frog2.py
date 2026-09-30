def main():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))

    dp = [(10**18) for _ in range(N)]
    dp[0] = 0

    for i in range(N-1):
        for j in range(1, K+1):
            if i+j < N:
                dp[i+j] = min(dp[i+j], dp[i]+abs(h[i]-h[i+j]))
    
    print(dp[-1])

main()
