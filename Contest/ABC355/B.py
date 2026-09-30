N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

from sortedcontainers import SortedList 

S = SortedList([])

for i in A:
    S.add(i)

for j in B:
    S.add(j)

A = set(A)
B = set(B)


ans = False
for k in range(len(S)-1):
    if S[k] in A and S[k+1] in A:
        ans = True

if ans:
    print("Yes")

else:
    print("No")