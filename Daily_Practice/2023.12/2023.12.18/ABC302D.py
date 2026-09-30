

from bisect import bisect_right 

def main():
    N, M, D = map(int, input().split())
    A = list(map(int, input().split()))
    B = sorted(list(map(int, input().split())))
    ans = 0
    for i in range(N):
        upper_limit = A[i] + D
        lower_limit = A[i] - D 

        upper_idx = bisect_right(B, upper_limit)-1 
        #print(upper_limit, upper_idx, "limit")
        if upper_idx >= 0 and B[upper_idx] >= lower_limit:
            #print(A[i], B[upper_idx], "upper")
            ans = max(ans, (A[i]+B[upper_idx]))

        lower_idx = bisect_right(B, lower_limit)
        if lower_idx <= 0 and B[lower_idx] <= upper_limit:
            #print(A[i], B[lower_idx], "lower")
            ans = max(ans, A[i]+B[lower_idx])
    
    print(ans if ans > 0 else -1)

main()