def check(x1,y1,x2,y2, t1,t2):
    dist = abs(x1-x2)+abs(y1-y2)
    time = t2-t1
    if dist > time:
        return False
    elif (time-dist) % 2 == 1:
        return False
    return True


def main():
    N = int(input())
    prev_t = 0
    prev_x = 0
    prev_y = 0
    for _ in range(N):
        t, x, y = map(int, input().split())
        if check(prev_x, prev_y, x, y, prev_t, t):
            prev_x = x
            prev_y = y
            prev_t = t
        else:
            return False
    
    return True 

if main():
    print("Yes")
else:
    print("No")

