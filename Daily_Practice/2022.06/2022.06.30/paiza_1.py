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

H, W = map(int, input().split())
ans = [[] for _ in range(H)]
def main():
    #　累積和とって二分探索
    for row in range(H):
        A = list(map(int, input().split()))
        AC = list(accumulate(A))
        if sum(A)//2 not in set(AC):
            return False
        ind = bisect_right(AC, sum(A)//2)
        for i in range(len(A)):
            if i < ind:
                ans[row].append('A')
            else:
                ans[row].append('B')
    return True

if main():
    print("Yes")
    for j in range(H):
        print(*ans[j], sep = "")
else:
    print("No")
    

            

