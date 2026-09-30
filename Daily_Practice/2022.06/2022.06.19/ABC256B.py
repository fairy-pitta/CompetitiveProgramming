def main():
    N = int(input())
    A = list(map(int, input().split()))[::-1]
    field = [[0] for i in range(N)]
    P = 0
    field[0][0] += A[0]
    if A[0] >= 4:
        P += 1
    for i in range(1, N):
        field[i][0] += field[i-1][0] + A[i]
        if field[i][0] >= 4:
            P += 1
    
    # print(field)
    return P

print(main())

