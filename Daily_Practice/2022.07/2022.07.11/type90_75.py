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



def primes_list(n):
    prime_flag = [1] * (n + 2)
    prime_flag[0] = 0
    prime_flag[1] = 0

    i = 2
    while i * i <= n+1:
        if prime_flag[i]:
            for j in range(2 * i, n + 2, i):
                prime_flag[j] = 0
        i += 1
    return [i for i in range(n + 2) if prime_flag[i]]

"""nを素因数分解"""
"""2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""

def factorization(n):
    arr = []
    temp = n
    start = int(n ** (0.5)) + 1
    for i in primes_list(start):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

## [[2, 3], [3, 1]] 
##  24 = 2^3 * 3^1



def main():
    N = int(input())
    li = factorization(N)
    exp = 0
    for i in li:
        exp += i[1]
    
    temp = 1
    ans = 0
    while exp > temp:
        temp *= 2
        ans += 1
    
    return ans


def solve():
    N = int(input())
    li = factorization(N)
    exp = 0
    for i in li:
        exp += i[1]
    
    A = [2 ** i for i in range(100)]
    ind = bisect_left(A, exp)
    return ind

    
print(solve())