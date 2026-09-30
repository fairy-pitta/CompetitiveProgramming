N = int(input())
A = list(map(int, input().split()))

F = [0]
for i in range(N):
    F.append(min(F[-1]+1, A[i]))

B = [0]
for j in reversed(range(N)):
    B.append(min(B[-1]+1, A[j]))

F = F[1:]
B = B[::-1]
ans = []

# print(F)
# print(B)

for k in range(N):
    ans.append(min(F[k], B[k]))




print(max(ans))

