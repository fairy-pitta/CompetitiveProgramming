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
# INF = 10 ** 9 + 1 



def main():
    N = int(input())
    if N % 2 != 0:
        print("")
        return False
    
    li = []
    for tuple in list(product((0,1), repeat = N)):
        num = Counter(tuple)
        if num[0] != num[1]:
            continue
        ans = ""
        left = 0
        right = 0
        flag = True
        for pa in list(tuple):
            if pa == 0:
                left += 1
                ans += "("
            else:
                right += 1
                ans += ")"
            
            if left < right:
                flag = False
                
        if flag:
            li.append(ans)
    
    li.sort()
    for element in li:
        print(element)
                
main()

            
    
