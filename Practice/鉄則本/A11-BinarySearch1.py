from bisect import bisect_right, bisect_left 
N, X = map(int, input().split())
A = list(map(int, input().split()))
print(bisect_right(A, X))