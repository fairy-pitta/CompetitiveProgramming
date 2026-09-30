N = int(input())

A = []
B = []

for _ in range(N):
    tmp =input()
    A.append(tmp)

for _ in range(N):
    tmp = input()
    B.append(tmp)

ans = [0, 0]
for row in range(N):
    for col in range(N):
        if A[row][col] != B[row][col]:
            ans[0] = row+1
            ans[1] = col+1
            break

print(*ans)
