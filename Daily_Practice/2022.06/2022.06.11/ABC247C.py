def main():
    N = int(input())
    dp = [[] for _ in range(N)]
    dp[0].append(1)

    for sn in range(1, N):
        dp[sn] = dp[sn-1] + [sn+1] + dp[sn-1]
    
    ans = dp[N-1]
    print(*ans)
main()