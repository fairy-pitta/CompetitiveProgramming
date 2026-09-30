from bisect import bisect_right 

def main():
    N, M, X = map(int, input().split())
    A = list(map(int, input().split()))
    idx = bisect_right(A, X)
    print(min(M-idx, idx))

main()

