from operator import itemgetter 
from collections import deque

def main():
    N = int(input())
    W = []
    for _ in range(N):
        a, b = map(int, input().split())
        W.append((a,b))
    
    W = deque(sorted(W, key=itemgetter(1,0)))
    cur, limit = W.popleft()

    while True:

        if len(W) == 0:
            break

        if cur <= limit:
            next_task, next_limit = W.popleft()
            cur += next_task
            limit = next_limit
        else:
            break
    
    if cur > limit:
        print("No")
    elif len(W) > 0:
        print("No")
    else:
        print("Yes")


main()
    
