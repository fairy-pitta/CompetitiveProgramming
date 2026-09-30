def main():
    N, M = map(int, input().split())
    D = list(map(int, input().split()))

    dp = [(False) for _ in range(N+1)]
    dp[0] = True 

    for i in range(N):
        for j in range(M):
            if i + D[j] <= N and dp[i]:
                dp[i+D[j]] = True
    
    return dp[-1]

if main():
    print("Yes")
else:
    print("No")
