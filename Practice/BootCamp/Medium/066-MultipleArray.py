from math import ceil 

def main():
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    
    cnt = 0
    for i in reversed(range(N)):
        A[i] += cnt
        if A[i]%B[i] == 0:
            continue

        diff = B[i] - (A[i]%B[i])
        cnt += diff

    print(cnt)

main()

