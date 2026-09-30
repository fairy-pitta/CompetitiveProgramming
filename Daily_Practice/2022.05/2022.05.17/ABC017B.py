def main():
    from collections import deque
    X = list(input())
    dq = deque(X)
    while True:
        if len(dq) == 0:
            break 
        if dq[-1] == "h" and len(dq) >= 2:
            dq.pop()
            if dq[-1] == "c":
                dq.pop()
            else:
                break 
        elif dq[-1] == "o":
            dq.pop()
        elif dq[-1] == "k":
            dq.pop()
        elif dq[-1] == "u":
            dq.pop()
        else:
            break 
    
    if len(dq) == 0:
        return "YES"
    else:
        return "NO"

print(main())
