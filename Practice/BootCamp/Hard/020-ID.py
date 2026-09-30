N, M = map(int, input().split())
city = []

for i in range(M):
    p, m = map(int, input().split())
    city.append([p, m, i])

from collections import defaultdict

d = defaultdict(list)
for j in range(len(city)):
    d[city[j][0]].append([city[j][1], city[j][2]])

ans = []
for key, value in d.items():
    v_list = sorted(value)
    for k in range(len(v_list)):
        id = str(key).zfill(6) + str(k+1).zfill(6)
        ans.append([v_list[k][1], id])

ans = sorted(ans)
for p in range(len(ans)):
    print(ans[p][1])    

