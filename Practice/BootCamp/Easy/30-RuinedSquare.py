
def main():
    x1, y1, x2, y2 = map(int, input().split())
    x3 = x2+y1-y2 
    y3 = y2-x1+x2
    x4 = x1+y1-y2
    y4 = y1-x1+x2
    print(x3, y3, x4, y4)

main()

from math import pi, cos, sin 

# (x,y) を(p, q)を中心に反時計回りに theta(radian) 回転させる
def anti_clockwise(x, y, p, q, theta):
    new_x = (x - p) * cos(theta) - (y - q) * sin(theta) + p
    new_y = (x - p) * sin(theta) + (y - q) * cos(theta) + q
    return (new_x, new_y)



