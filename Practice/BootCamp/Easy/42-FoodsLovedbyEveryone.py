def main():
    N, M = map(int, input().split())
    foods_list = [(0) for _ in range(M+1)]
    for _ in range(N):
        a = list(map(int, input().split()))
        for item in range(1, len(a)):
            foods_list[a[item]] += 1
    cnt = 0
    for food in range(M+1):
        if foods_list[food] == N:
            cnt += 1
    
    print(cnt)

main()