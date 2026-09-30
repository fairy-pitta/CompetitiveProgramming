from collections import defaultdict

d = defaultdict(int)

N, M = map(int, input().split())
A = list(map(int, input().split()))

for _ in range(N):
    li = list(map(int, input().split()))
    for nut in range(M):
        d[nut] += li[nut]

ans = True
for j in range(len(A)):
    if d[j] < A[j]:
        ans = False
        #print(d[j], A[j])

#print(d)
if ans:
    print("Yes")
else:
    print("No")