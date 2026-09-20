N = int(input())
A = list(map(int, input().split()))

from collections import defaultdict 

d = defaultdict(lambda: {7: 0, 5: 0, 3: 0})

for i in range(N):
    if not A[i] % 7:
        d[A[i]//7][7] += 1
    elif not A[i] % 5:
        d[A[i]//5][5] += 1
    elif not A[i] % 3:
        d[A[i]//3][3] += 1

ans = 0
for value in d.values():
    ans += value[7] * value[5] * value[3]

print(ans)

