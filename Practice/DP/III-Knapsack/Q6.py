# 部分和問題（応用2）

def main():
    N, A, B = map(int, input().split())
    X = list(map(int, input().split()))

    dp = [[(False) for _ in range(A)] for _ in range(N+1)]
    dp[0][0] = True 

    for card in range(N):
        for num in range(A):

            if not dp[card][num]:
                continue 

            dp[card+1][num] = True 
            dp[card+1][(num+X[card])%A] = True 
    
    if dp[-1][B]:
        print("Yes")
    else:
        print("No")

main()
