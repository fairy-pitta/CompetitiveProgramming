
def main():
    N = int(input())
    X = list(map(int, input().split()))

    li = []
    for i in range(N):
        li.append([X[i], i])
    
    li = sorted(li)
    ans = [(0) for _ in range(N)]

    for j in range(N):
        if j < N//2:
            ans[li[j][1]] = li[N//2][0]
        else:
            ans[li[j][1]] = li[N//2-1][0]
    
    for k in ans:
        print(k)

main()

