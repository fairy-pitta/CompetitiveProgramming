
def main():
    A, B, K = map(int, input().split())
    for i in range(A, B+1):
        if i <= A+K-1:
            print(i)
        elif i >= B-K+1:
            print(i)

main()