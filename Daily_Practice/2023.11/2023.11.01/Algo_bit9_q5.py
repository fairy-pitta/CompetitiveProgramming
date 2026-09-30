
def main():
    N, X = map(int, input().split())

    ans = []

    for i in range(N):
        if X & (1<<i) > 0:
            ans.append(i)
    
    print(ans)

main()
