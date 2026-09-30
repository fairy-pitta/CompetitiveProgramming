def main():
    D = int(input())
    N = int(input())
    num = [(0) for _ in range(D+1)]
    for _ in range(N):
        l, r = map(int, input().split())
        l -= 1
        num[l] += 1
        num[r] -= 1
    
    cnt = 0

    for i in range(D):
        cnt += num[i]
        print(cnt)
    

main()


