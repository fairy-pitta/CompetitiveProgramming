def main():
    H, W = map(int, input().split())
    field = []
    for _ in range(H):
        c = list(input())
        field.append(c)
    
    dp = [[(0) for _ in range(W)] for _ in range(H)]
    dp[0][0] = 1
    ans = 1

    for rowwise in range(1,H):
        if field[rowwise - 1][0] == ".":
            dp[rowwise][0] = dp[rowwise-1][0] + 1
            ans = max(ans, dp[rowwise][0])
        else:
            break 
    for colwise in range(1,W):
        if field[0][colwise - 1] == ".":
            dp[0][colwise] = dp[0][colwise-1] + 1
            ans = max(ans, dp[0][colwise])
        else:
            break 


    for row in range(1, H):
        for col in range(1, W):
            if field[row][col] == ".":
                dp[row][col] = max(dp[row-1][col], dp[row][col-1]) + 1
                ans = max(ans, dp[row][col])
            else:
                continue

    return ans 
  
print(main())
    
