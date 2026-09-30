def main():
    N, M = map(int, input().split())
    X = sorted(list(map(int, input().split())))

    gap = []
    for i in range(1, M):
        gap.append(abs(X[i]-X[i-1]))
    
    if N >= M:
        print(0)
    else:
        ans = 0
        gap = sorted(gap)
        for i in range(M-N):
            ans += gap[i]
        
        print(ans)


main()

