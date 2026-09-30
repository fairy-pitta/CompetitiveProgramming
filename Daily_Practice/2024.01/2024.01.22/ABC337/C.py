N = int(input())
A = list(map(int, input().split()))

G = [[] for _ in range(N+1)]

for i in range(N):
    index = i+1
    person = A[i]
    if person == -1:
        person = 0
    G[person].append(index)



ans = []
cur = 0

while True:

    if len(ans) >= N:
        break 
    ans.append(G[cur][0])
    cur = G[cur][0]

print(*ans)

