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

from itertools import groupby

# RUN LENGTH ENCODING str -> list(tuple())
# example) "aabbbbaaca" -> [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)] 
def runLengthEncode(S: str) -> "List[tuple(str, int)]":
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res

def main():
    S = str(input())
    T = str(input())
    s = runLengthEncode(S)
    t = runLengthEncode(T)
    # print(s)
    # print(t)

    if len(s) != len(t):
        return False
    for i in range(len(s)):
            s_letter, s_num = s[i]
            t_letter, t_num = t[i]
            if s_letter != t_letter:
                # print("error 1")
                # print(s_letter, t_letter)
                return False
            elif t_num < s_num:
                # print("error 2")
                return False


from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

def solve():
    N = int(input())
    S = str(input())
    li = runLengthEncode(S)
    if N >= 2:
        total = cmb(N, 2)
    else:
        total = 0
    ans = 0
    for tup in li:
        key, value = tup
        if value >= 2:
            ans += cmb(value, 2)
    
    return total - ans 

print(solve())


