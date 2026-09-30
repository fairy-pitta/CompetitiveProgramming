def main():
    N = int(input())
    meals = []
    for _ in range(N):
        meals.append(list(map(int, input().split())))

    dp = [[0, 0] for _ in range(N+1)]
    dp[0][0] = 0

    for i in range(N):
        # 食べないとき
        dp[i+1][0] = dp[i][0]
        dp[i+1][1] = dp[i][1]

        # 食べるとき
        ## 毒があります
        if meals[i][0] == 1:
            dp[i+1][1] = max(dp[i+1][1], dp[i][0]+meals[i][1]) 
        ## 解毒剤があります
        else:
            dp[i+1][0] = max(dp[i+1][0], max(dp[i][0], dp[i][1])+meals[i][1])
    
    print(max(dp[-1]))

main()
