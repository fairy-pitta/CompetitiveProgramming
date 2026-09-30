N, X, Y = map(int, input().split())
red = [N, 1]
blue = [N, 0]

while True:
    if red[1] == 0:
        break
    if blue[0] == 1:
        break 
    if red[0] == 1:
        break 
    
    # red transformation
    red[0] -= 1
    blue[1] += red[1]*X
    
    # blue transformation 
    red[1] += blue[1]
    blue[1] = blue[1]*Y
    blue[0] -= 1

print(blue[1])
