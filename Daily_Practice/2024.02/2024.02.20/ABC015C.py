N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]

from itertools import product 

li = list(product(list(range(K)), repeat = N))

flag = True 

for pos in li:
    ans = 0
    for i in range(N):
        ans ^= T[i][pos[i]]
    if ans == 0:
        flag = False

if flag:
    print("Nothing")
else:
    print("Found")