from collections import deque

def main():
    s = list(str(input())[::-1])
    s = deque(s)
    while True:
        if len(s) == 0:
            break 
        if s[0] == "a":
            s.popleft()
        elif s[-1] == "a":
            s.pop()
        else:
            break 
    
    # print(s)
    s = "".join(s)
    # print(s)
    if str(s) == str(s)[::-1]:
        return True
    else:
        return False

if main():
    print("Yes")
else:
    print("No")
    