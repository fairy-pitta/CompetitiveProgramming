N, D, P = map(int, input().split())
F = sorted(list(map(int, input().split())))
B = [0]
for i in F:
    B.append(B[-1]+i)

ans = 10**18

for i in range(N//D+2):
    cost = P*i
    days = N-D*i
    if days > 0:
        cost += B[days]
    ans = min(ans, cost)

print(ans)

