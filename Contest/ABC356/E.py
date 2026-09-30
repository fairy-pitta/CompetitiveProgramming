N = int(input())

A = list(map(int, input().split()))
A.sort()

B = [0]
for i in A:
    B.append(B[-1]+i)

s = 0
for j in range(len(A)):
    s += (B[-1]-B[j+1]) // A[j]

print(s)