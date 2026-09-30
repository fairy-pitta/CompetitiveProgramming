from collections import defaultdict 

N = int(input())
d = defaultdict(int)

for _ in range(N):
  a = int(input())
  d[a] += 1 

print(len(d))
  