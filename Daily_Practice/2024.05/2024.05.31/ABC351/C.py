from collections import deque 

N = int(input())
A = list(map(int, input().split()))
d = deque([A[0]])
f = deque(A[1:])


while f:
    #print(d, f)
    if not d:
        d.append(f[0])
        f.popleft()
    
    if not f:
        break
    
    if d[-1] == f[0]:
        d.pop()
        f[0] += 1
    else:
        d.append(f[0])
        f.popleft()

print(len(d))




