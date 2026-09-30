Q = int(input())
from collections import defaultdict
stack = defaultdict()
for _ in range(Q):
    s = list(map(int, input().split()))
    if s[0] == 1:
        stack[s[1]] += 1
    elif s[0] == 3:
        print(max(stack) - min(stack))
    else:
        x = s[1]
        c = s[2]
        if stack[x] >= c:
            stack[x] -= c 
        else:
            stack[x] = 0
        


