N = int(input())
A = list(map(int, input().split()))

ans = 10 ** 9

for i in range(N):
  cnt = 0
  for _ in range(40):
    if not A[i] % 2:
      cnt += 1
      A[i] = A[i] // 2
    else:
      break
  
  ans = min(cnt, ans)

print(ans)
