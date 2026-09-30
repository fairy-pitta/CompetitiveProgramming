def main():
    N, Q = map(int, input().split())
    A = [i for i in range(1, N+1)]
    for j in range(Q):
        x = int(input())
        index = A.index(x)
        if index == (N-1):
            A[N-2], A[N-1] = A[N-1], A[N-2]
        else:
            A[index], A[index+1] = A[index+1], A[index]
        # print(A)
    
    print(*A)
main()