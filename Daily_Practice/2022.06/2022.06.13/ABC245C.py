from selectors import EpollSelector


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    dp_A = [False] * N
    dp_B = [False] * N
    dp_A[0] = True
    dp_B[0] = True 

    for i in range(N-1):
        # can use A 
        if dp_A[i]:
            dp_A[i+1] = dp_A[i+1] or abs(A[i] - A[i+1]) <= K
            dp_B[i+1] = dp_B[i+1] or abs(A[i] - B[i+1]) <= K
        # can use B
        if dp_B[i]:
            dp_A[i+1] = dp_A[i+1] or abs(B[i] - A[i+1]) <= K
            dp_B[i+1] = dp_B[i+1] or abs(B[i] - B[i+1]) <= K
    
    ans = dp_A[N-1] or dp_B[N-1]
    if ans:
        print("Yes")
    else:
        print("No")


main()






