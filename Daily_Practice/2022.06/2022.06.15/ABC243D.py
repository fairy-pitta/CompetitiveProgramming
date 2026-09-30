from collections import deque
from selectors import EpollSelector

def main():
    N, X = map(int, input().split())
    S = list(input())
    # for shortened list 
    d = deque()
    # won't be empty 
    d.append("ins")

    # judge if the moves can be shortened 
    for i in range(N):
        if i == 0:
            d.append(S[0])
        else:
            if S[i] == "U":
                if d[-1] == "L" or d[-1] == "R":
                    d.pop()
                else:
                    d.append(S[i])
            else:
                d.append(S[i])
    
    # print(d)
    ans = X
    for c in d:
        if c == "L":
            ans = 2 * ans 
        elif c == "R":
            ans = 2 * ans + 1
        elif c == "U":
            ans = ans // 2
        else:
            continue
        # print(ans)
    
    return ans 

print(main())


                

