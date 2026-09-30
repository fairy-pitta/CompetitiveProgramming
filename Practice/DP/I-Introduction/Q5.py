
def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [(10**18) for _ in range(N)]
    dp[0] = 0
    
    for i in range(1, len(dp)):
        for j in range(1, M+1):
            if i-j >= 0:
                dp[i] = min(dp[i], dp[i-j]+j*A[i])
    
    print(dp[-1])

main()
