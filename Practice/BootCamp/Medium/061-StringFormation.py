from collections import deque 

def main():
    S = deque(input())
    Q = int(input())
    isreversed = False
    for _ in range(Q):
        t = list(map(str, input().split()))
        if t[0] == "1":
            isreversed = not isreversed 
        else:
            if t[1] == "1":
                if isreversed:
                    S.append(t[2])
                else:
                    S.appendleft(t[2])
            else:
                if isreversed:
                    S.appendleft(t[2])
                else:
                    S.append(t[2])

    ans = "".join(list(S)[::-1] if isreversed else list(S))
    print(ans)

main()
