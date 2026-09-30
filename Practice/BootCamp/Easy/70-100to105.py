
def main():
    X = int(input())

    dp = [(0) for _ in range(X+1)]
    dp[0] = 1

    for i in range(X+1):
        if dp[i]:
            for j in range(100, 106):
                if i+j <= X:
                    dp[i+j] = 1
    
    print(dp[X])

main()


