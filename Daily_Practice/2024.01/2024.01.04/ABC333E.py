from collections import defaultdict 

N = int(input())
TX = reversed([list(map(int, input().split())) for _ in range(N)])
portion = defaultdict(int)
k = 0
num = 0
actions = []

for t, x in TX:
    if t == 1:
        if portion[x] > 0:
            portion[x] -= 1
            num -= 1
            actions.append(1)
        else:
            actions.append(0)
    else:
        portion[x] += 1
        num += 1
        k = max(k, num)

if sum(portion.values()) == 0:
    print(k)
    print(*reversed(actions))
else:
    print(-1)
        

