def main():
    N = int(input())
    A = []
    for _ in range(N):
        a = int(input())
        A.append(a)
    A_sorted = sorted(A, reverse = True)
    for item in range(N):
        if A[item] == A_sorted[0]:
            print(A_sorted[1])
        else:
            print(A_sorted[0])

main()