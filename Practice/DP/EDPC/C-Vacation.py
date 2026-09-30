def main():
    N = int(input())
    h = [list(map(int, input().split())) for _ in range(N)]

    dp = [[(0) for _ in range(3)] for _ in range(N)]
    dp[0] = h[0]

    for day in range(1, N):
        dp[day][0] = max(dp[day-1][1], dp[day-1][2]) + h[day][0]
        dp[day][1] = max(dp[day-1][0], dp[day-1][2]) + h[day][1]
        dp[day][2] = max(dp[day-1][0], dp[day-1][1]) + h[day][2]
    
    print(max(dp[-1]))

main()
    