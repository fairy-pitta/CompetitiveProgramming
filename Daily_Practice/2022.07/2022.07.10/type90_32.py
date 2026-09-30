from collections import deque, Counter, defaultdict
from operator import itemgetter 
from bisect import bisect_right, bisect_left 
from itertools import combinations, permutations, accumulate, product
import heapq
# from numpy import base_repr
from copy import deepcopy
import sys
# sys.setrecursionlimit(10**6)
from math import gcd, log2, log10
def my_lcm(a, b):
    return a * b // gcd(a, b)
def my_ceil(N, W):
    return (-(-N//W))
def printout(func):
    if func: print("Yes")
    else: print("No")

# MOD = 998244353
# MOD = 1000000007
INF = 10 ** 9 + 1 

def main():
    N = int(input())
    A = []
    for _ in range(N):
        a = list(map(int, input().split()))
        A.append(a)
    players = [i for i in range(1, N+1)]
    M = int(input())
    graph = [set() for _ in range(N+1)]
    for _ in range(M):
        x, y = map(int, input().split())
        graph[y].add(x)
        graph[x].add(y)
    
    time = INF 

    for seq in list(permutations(players)):
        order = list(seq)
        t = 0
        possible  = True
        # print(order)
        for i in range(N):
            if i == N-1 and possible:
                t += A[order[i]-1][i]
                # print("added last", A[order[i]-1][i])
            elif i == N-1:
                continue
            elif order[i+1] in graph[order[i]]:
                # print("not here tho?")
                possible = False
            elif possible:
                t += A[order[i]-1][i]
                # print("added middle", A[order[i]-1][i])
        
        # print("this is t", t)
        if possible and t > 0:
            time = min(time, t)
    
    if time == INF:
        return -1 
    else:
        return time

print(main())
    

    