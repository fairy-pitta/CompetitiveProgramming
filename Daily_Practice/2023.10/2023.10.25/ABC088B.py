N = int(input())
A = sorted(list(map(int, input().split())), reverse = True)
ans = 0
for i in range(N):
  if not i % 2:
    ans += A[i]
  else:
    ans -= A[i]

print(ans)
