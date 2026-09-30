N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = [0]
for i in A:
    B.append(B[-1]+i)

for _ in range(Q):
    l, r = map(int, input().split())
    print(B[r]-B[l-1])

