from collections import deque, Counter, defaultdict
from operator import itemgetter 
from bisect import bisect_right, bisect_left 
from itertools import combinations, permutations, accumulate, product
import heapq
# from numpy import base_repr
from copy import deepcopy
import sys
# sys.setrecursionlimit(10**6)
from math import gcd
def my_lcm(a, b):
    return a * b // gcd(a, b)
def my_ceil(N, W):
    return (-(-N//W))
def printout(func):
    if func: print("Yes")
    else: print("No")

def main():
    N, X = map(int, input().split())
    stages = []
    game = []
    for i in range(N):
        a, b = map(int, input().split())
        stages.append(a+b)
        if i == 0:
            m = b
            game.append(m)
        else:
            m = min(m, b)
            game.append(m)
  
    stages = list(accumulate(stages))
    op = []
    for i in range(N):
        time = stages[i]
        which = game[i]
        time += (X - i - 1) * which
        op.append(time)
    
    # print(op)
    return min(op)

print(main())



