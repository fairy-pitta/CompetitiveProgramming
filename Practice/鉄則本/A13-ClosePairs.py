from bisect import bisect_right, bisect_left 

N, K = map(int, input().split())
A = sorted(list(map(int, input().split())))

cnt = 0
for i in range(N):
    upper = A[i]+K
    lower = A[i]-K
    cnt += (bisect_right(A, upper)-bisect_left(A, lower))-1

print(cnt//2)



