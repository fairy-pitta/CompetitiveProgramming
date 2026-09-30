X, Y, A, B, C = map(int, input().split())
p = sorted(list(map(int, input().split())), reverse=True)[:X]
q = sorted(list(map(int, input().split())), reverse=True)[:Y]
r = sorted(list(map(int, input().split())))

ans = 0

li = sorted(p+q+r, reverse=True)
for i in range(X+Y):
    ans += li[i]

print(ans)