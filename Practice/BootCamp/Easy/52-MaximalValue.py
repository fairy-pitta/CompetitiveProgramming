def main():
    N = int(input())
    B = list(map(int, input().split()))
    A = [(0) for _ in range(N)]
    for i in range(N):
        if i == 0:
            A[i] = B[0]
        elif i == N-1:
            A[i] = B[-1]
        else:
            A[i] = min(B[i], B[i-1])
    
    print(sum(A))

main()