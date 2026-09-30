# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_d

N = int(input())
S = input()

from collections import defaultdict

d = defaultdict(list)
ans = 0

for i in range(N):
    d[S[i]].append(i)

for j in range(10**3):
    pin = str(j).zfill(3)
    if d[pin[0]] and d[pin[2]]:
        first_index = min(d[pin[0]]) 
        last_index = max(d[pin[2]]) 

        if pin[1] in S[first_index+1:last_index]:
            ans += 1

print(ans)

