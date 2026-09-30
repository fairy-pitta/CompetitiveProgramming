S = str(input())

confirmed = set()
unsure = set()

for j in range(10):
    if S[j] == "o":
        confirmed.add(j)
    elif S[j] == "?":
        unsure.add(j)

from itertools import product

pos = list(product([0,1,2,3,4,5,6,7,8,9], repeat=4))
ans = 0

for i in pos:
    flag = True
    for k in list(confirmed):
        if k not in i:
            flag = False
    for num in i:
        if (int(num) not in confirmed) and (int(num) not in unsure):
            flag = False
    if flag:
        ans += 1 


print(ans)