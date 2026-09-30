from sortedcontainers import SortedSet

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    new_P = [(0) for _ in range(N)]

    if K == 1:
        return 0

    for i in range(N):
        new_P[P[i]-1] = i

    S = SortedSet([])
    for j in range(K):
        S.add(new_P[j])


    ans = abs(S[0]-S[-1])


    for i in range(1,N-K+1):

        S.discard(new_P[i-1])
        S.add(new_P[i+K-1])

        ans = min(ans, abs(S[0] - S[-1]))


    return ans

print(main())

