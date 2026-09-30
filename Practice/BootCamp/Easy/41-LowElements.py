def main():
    N = int(input())
    P = list(map(int, input().split()))
    min_p = P[0]
    cnt = 0
    for i in range(N):
        if P[i] <= min_p:
            cnt += 1
            min_p = P[i]
    
    print(cnt)

main()
