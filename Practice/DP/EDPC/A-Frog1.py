def main():
    N = int(input())
    h = list(map(int, input().split()))
    dp = [(10**18) for _ in range(N)]
    dp[0] = 0

    for i in range(N-1):
        dp[i+1] = min(dp[i+1], dp[i]+abs(h[i]-h[i+1]))
        if i+2 < N:
            dp[i+2] = min(dp[i+2], dp[i]+abs(h[i]-h[i+2]))
    
    print(dp[-1])

main()