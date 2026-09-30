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
    N = int(input())
    li = []
    for _ in range(N):
        a, b = map(int, input().split())
        li.append([a,b])
    li = sorted(li, key = itemgetter(1))
    can = True
    time = 0
    for task in li:
        t, due = task[0], task[1]
        time += t 
        if time > due:
            can = False
    
    return can 

printout(main())

