def main():
    N = int(input())
    B = list(map(int, input().split()))

    ans = []
    for _ in range(N):
        for j in reversed(range(len(B))):

            if B[j] == j+1:
                ans.append(j+1)
                del B[j]
                break
    
    if len(B) > 0:
        print(-1)
    else:
        for k in ans[::-1]:
            print(k)

main()
