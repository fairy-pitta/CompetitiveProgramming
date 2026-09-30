#https://atcoder.jp/contests/code-festival-2017-qualc/tasks/code_festival_2017_qualc_c

from collections import deque

s = list(input())
d = deque(s)
flag = True
ans = 0

while d:

    if len(d) == 1:
        break

    head = d.popleft()
    tail = d.pop()

    if head == tail:
        continue 
    elif head == "x":
        d.appendleft(head)
        d.append(tail)
        d.append("x")
        ans += 1
    elif tail == "x":
        d.append(tail)
        d.appendleft(head)
        d.appendleft("x")
        ans += 1
    else:
        flag = False 
        break 

if flag:
    print(ans)
else:
    print(-1)