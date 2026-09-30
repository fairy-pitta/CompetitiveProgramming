def main():
    N = int(input())
    P = list(map(int, input().split()))
    cnt = 0
    min_item = P[0]
    for i in range(N):
        if P[i] <= min_item:
            cnt += 1
            min_item = min(min_item, P[i])

    
    print(cnt)

main()