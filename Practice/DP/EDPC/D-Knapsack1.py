def main():
    N, W = map(int, input().split())
    v = [list(map(int, input().split())) for _ in range(N)]

    dp = [[0] * (W + 1) for _ in range(N + 1)]

    for item in range(N):
        for weight in range(W + 1):
            dp[item + 1][weight] = max(dp[item + 1][weight], dp[item][weight])

            new_weight = weight + v[item][0]
            if new_weight <= W:
                dp[item + 1][new_weight] = max(
                    dp[item + 1][new_weight],
                    dp[item][weight] + v[item][1]
                )

    print(max(dp[-1]))

main()


