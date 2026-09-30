S = input()
T = int(input())

def dist(x, y):
    return abs(x) + abs(y)

cnt = 0
x = 0
y = 0

for i in S:
    if i == "L":
        x -= 1
    elif i == "R":
        x += 1
    elif i == "U":
        y += 1
    elif i == "D":
        y -= 1
    else:
        cnt += 1

pos = [dist(x+cnt, y), dist(x-cnt, y), dist(x, y+cnt), dist(x, y-cnt)]

if T == 1:
    print(max(pos))
else:
    if dist(x, y) >= cnt:
        print(dist(x, y) - cnt)
    elif (cnt - dist(x, y)) % 2 == 0:
        print(0)
    else:
        print(1)