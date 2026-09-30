from operator import itemgetter
#key=itemgetter(0, 1)

N = int(input())
A = list(map(int, input().split()))
Adx = sorted([[A[i], i] for i in range(N)])

for j in range(N):
    if j == 0:
        Adx[0].append(1)
    else:
        if Adx[j][0] > Adx[j-1][0]:
            Adx[j].append(Adx[j-1][2]+1)
        else:
            Adx[j].append(Adx[j-1][2])

Adx = sorted(Adx, key=itemgetter(1))
ans = []
for k in range(N):
    ans.append(Adx[k][2])

print(*ans)