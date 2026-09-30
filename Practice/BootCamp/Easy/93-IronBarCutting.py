
def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_accum = [0]
    for i in range(N):
        A_accum.append(A[i]+A_accum[-1])

    ans = 10**18
    for j in range(len(A_accum)):
        diff = abs(A_accum[j] - (A_accum[-1] - A_accum[j]))
        ans = min(ans, diff)
    
    print(ans)

main()