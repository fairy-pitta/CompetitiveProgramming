from collections import deque, Counter, defaultdict
from operator import itemgetter 
from bisect import bisect_right, bisect_left 
from itertools import combinations, permutations, accumulate, product
import heapq
from copy import deepcopy
import sys
sys.setrecursionlimit(10**6)
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
    first = [(0) for _ in range(N+1)] 
    second = [(0) for _ in range(N+1)]
    for i in range(1, N+1):
        grp, score = map(int, input().split())
        if grp == 1:
            first[i] = score
        else:
            second[i] = score
    first = list(accumulate(first))
    second = list(accumulate(second))

    # print(first)
    # print(second)

    Q = int(input())
    for _ in range(Q):
        l, r = map(int, input().split())
        one = first[r] - first[l-1]
        two = second[r] - second[l-1]
        print(one, two)

main()

