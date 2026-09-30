def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    monster = 0

    for yusha in range(N):
        # この街すべて制圧可能
        if B[yusha] > A[yusha]:
            B[yusha] -= A[yusha]
            monster += A[yusha]

            # まだ体力があるが次の街全て制圧はできない
            if B[yusha] <= A[yusha+1]:
                monster += B[yusha]
                A[yusha+1] -= B[yusha]
            # 次の街も全て制圧可能
            else:
                monster += A[yusha+1]
                A[yusha+1] = 0
        # この街ちょいと厳しい
        else:
            monster += B[yusha]
        
    print(monster)

main()

