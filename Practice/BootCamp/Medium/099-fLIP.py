def main():
    N, M, K = map(int, input().split())

    flag = False
    for row in range(N+1):
        for col in range(M+1):
            if row*(M-col) + (N-row)*col == K:
                flag = True
    
    if flag:
        print("Yes")
    else:
        print("No")

main()