N, A, B = map(int, input().split())

ans = 0

for i in range(N+1):
  li = [int(z) for z in list(str(i))]
  if A <= sum(li) <= B:
    ans += i

print(ans)