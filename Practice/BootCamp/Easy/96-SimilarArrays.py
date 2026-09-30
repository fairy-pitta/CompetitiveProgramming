def main():
    N = int(input())
    A = list(map(int, input().split()))

    cnt = 1

    for i in range(N):
        if not A[i]%2:
            cnt *= 2
    
    print(3**N-cnt)

main()


