from collections import defaultdict

N = int(input())
w = list()
for _ in range(n):
    w1, w2 = map(int, input().split())
    w.append([w1, w2])

d = defaultdict(int)

for i in range(N):
    for j in range(9):
        d[(w[i][1] + j) % 24] += w[i][0]

print(max(d.values()))

