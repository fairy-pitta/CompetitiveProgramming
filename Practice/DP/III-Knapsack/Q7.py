# ボールと２つの箱

def main():
    N = int(input())
    W = list(map(int, input().split()))

    dp = [[(False)for _ in range(sum(W)+1)] for _ in range(N+1)]
    dp[0][0] = True

    for i in range(N):
        for j in range(sum(W)+1):
            if not dp[i][j]:
                continue 

            dp[i+1][j+W[i]] = True 
            dp[i+1][abs(j-W[i])] = True
    
    ans = 0
    for i in dp[-1]:
        if not i:
            ans += 1
        else:
            break
    
    print(ans)

main()

