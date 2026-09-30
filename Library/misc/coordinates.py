from math import pi, cos, sin 

# (x,y) を(p, q)を中心に反時計回りに theta(radian) 回転させる
def anti_clockwise(x, y, p, q, theta):
    new_x = (x - p) * cos(theta) - (y - q) * sin(theta) + p
    new_y = (x - p) * sin(theta) + (y - q) * cos(theta) + q
    return (new_x, new_y)


def clockwise(x, y, p, q, theta):
    new_theta = 2 * pi - theta 
    return anti_clockwise(x, y, p, q, new_theta)