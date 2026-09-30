
def main():
    N, P, Q = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for first in range(N-4):
        for second in range(first+1, N-3):
            for third in range(second+1, N-2):
                for forth in range(third+1, N-1):
                    for fifth in range(forth+1, N):
                        if A[first] * A[second] % P * A[third] % P * A[forth] % P * A[fifth] % P == Q:
                            ans += 1
    
    return ans 

print(main())
    