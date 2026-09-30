def main():
    N = int(input())
    a = list(map(int, input().split()))
    idx = 1
    cnt = 0
    for i in range(N):
        if a[i] == idx:
            cnt += 1
            idx += 1
    
    if cnt == 0:
        print(-1)
    else:
        print(N-cnt)
main()