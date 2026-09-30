from itertools import product
from collections import deque

def main():
    N = int(input())
    L = []
    choices = list(product([0,1], repeat = N))
    # print(choices)

    for _ in range(N):
        h, l, w = map(int, input().split())
        L.append([l, w, h])
    L = sorted(L)
    print(L)
    ans = 0
    for c in choices:
        flag = True
        height = 0
        d = deque()
        for block in range(N):
            if c[block] == 0:
                continue
            if d:
                cur = L[block]
                pre = d.pop()
                if cur[0] < pre[0] or cur[1] < pre[1]:
                    flag = False
                    break 
                d.append(pre)
                d.append(c)
            else:
                d.append(L[block])
            
            height += L[block][2]

        if flag:
            ans = max(ans, height)
            if height == 1614:
                print(c, flag)
    
    print(ans)

main()
