N, M = map(int, input().split())

A = [list(input()) for _ in range(N)]
B = [list(input()) for _ in range(M)]
ans = False
for r in range(N-M+1):
    for c in range(N-M+1):
        flag = True
        for sr in range(M):
            for sc in range(M):
                if B[sr][sc] != A[r+sr][c+sc]:
                    flag = False
        
        ans = ans or flag

if ans:
    print("Yes")
else:
    print("No")

            