from collections import deque, Counter, defaultdict
from operator import itemgetter 
from bisect import bisect_right, bisect_left 
from itertools import combinations, permutations, accumulate, product
import heapq
# from numpy import base_repr
from copy import deepcopy
from re import L
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
# INF = 10 ** 9 + 7
def Dec_to_N(num, base):
    if num >= base:
        yield from Dec_to_N(num // base, base)
    yield num % base

def N_to_Dec(digits, base):
    num = 0
    for digit in digits:
        num = num * base + int(digit)
    return num

def base10to(n, b):
    if n // b:
        return base10to(n // b, b) + str(n % b)
    return str(n % b)

def main():
    N, K = map(int, input().split())
    t = str(N)
    for _ in range(K):
        converted_to_10 = int(t, 8)
        converted_to_9 = str(base10to(converted_to_10, 9))
        new = ""
        for i in range(len(converted_to_9)):
            if converted_to_9[i] == 8:
                new += "5"
            else:
                new += str(converted_to_9[i])
        t = "".join(new)
    return t


print(main())
