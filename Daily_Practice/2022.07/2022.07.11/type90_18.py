from collections import deque, Counter, defaultdict
from operator import itemgetter 
from bisect import bisect_right, bisect_left 
from itertools import combinations, permutations, accumulate, product
import heapq
# from numpy import base_repr
from copy import deepcopy
import sys
# sys.setrecursionlimit(10**6)
from math import degrees, pi, cos, sin, atan2, sqrt, radians
def my_lcm(a, b):
    return a * b // gcd(a, b)
def my_ceil(N, W):
    return (-(-N//W))
def printout(func):
    if func: print("Yes")
    else: print("No")

# MOD = 998244353
MOD = 1000000007
# INF = 10 ** 9 + 1 

def i_int(): return int(input())
def i_map(): return map(int, input().split())

from math import pi, cos, sin 

# (x,y) を(p, q)を中心に反時計回りに theta(radian) 回転させる
def anti_clockwise(x, y, p, q, theta):
    new_x = (x - p) * cos(theta) - (y - q) * sin(theta) + p
    new_y = (x - p) * sin(theta) + (y - q) * cos(theta) + q
    return (new_x, new_y)


def clockwise(x, y, p, q, theta):
    new_theta = 2 * pi - theta 
    return anti_clockwise(x, y, p, q, new_theta)
    
def coor(E, L, T):
    theta = 2 * pi - (2 * pi * (E/T)) 
    x = 0
    y = - (L / 2)
    new_x = x * cos(theta) - y * sin(theta)
    new_y = x * sin(theta) + y * cos(theta)
    new_y += L/ 2
    return (new_x, new_y)

def coordinate(E, L, T):
    theta = 2 * pi * E / T
    new_x = - (L / 2) * sin(theta)
    new_y = (L / 2) - (L // 2) * cos(theta)
    return (new_x, new_y)

def ang(x1, y1, z1, x2, y2):
    dist = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) 
    return atan2(z1, dist)

def solve():
    T = i_int()
    L, X, Y = i_map()
    Q = i_int()
    for i in range(Q):
        e = i_int()
        y1, z1 = coor(e, L, T)
        ans = ang(0, y1, z1, X, Y)
        print(degrees(ans))

solve()







            




