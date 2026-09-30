from collections import deque 

S = deque(list(str(input())))
T = deque(list(str(input())))

ans = []

for i in range(len(T)):
    if len(S) == 0:
        continue
    elif S[0] != T[0]:
        T.popleft()
    else:
        ans.append(i+1)
        S.popleft()
        T.popleft()

print(*ans)