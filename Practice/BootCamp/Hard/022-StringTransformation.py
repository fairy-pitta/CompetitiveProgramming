S = input()
T = input()

from collections import defaultdict

sd = defaultdict(list)
td = defaultdict(list)

for i in range(len(S)):
    sd[S[i]].append(i)
    td[T[i]].append(i)


sd_list = list(sd.values())
td_list = list(td.values())

if sd_list == td_list:
    print("Yes")
else:
    print("No")