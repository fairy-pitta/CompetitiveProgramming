N = int(input())
P = list(map(int, input().split()))
minimum = P[0]
ans = 1

for i in range(1, N):
  #print(P[i], minimum)
  if P[i] <= minimum:
    ans += 1 
  minimum = min(minimum, P[i])
  

print(ans)