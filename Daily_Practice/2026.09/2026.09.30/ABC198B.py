# ABC198B  灰 (diff 0 / 100pt)
# https://atcoder.jp/contests/abc198/tasks/abc198_b




## frequently used functions 
from collections import deque, Counter, defaultdict
from operator import itemgetter 
from bisect import bisect_right, bisect_left 
from itertools import combinations, permutations, accumulate, product, groupby
import heapq
# from numpy import base_repr
from copy import deepcopy
import sys
# sys.setrecursionlimit(10**9)
from math import gcd, log2, log10
from functools import lru_cache, reduce 

def is_palindrome(s):
    i, j = 0, len(s) - 1  
    is_palindrome = True  
    while i < j:
        if s[i] != s[j]:  
            is_palindrome = False
            break
        i += 1
        j -= 1

    return is_palindrome

def main():
    N = str(input())
    leading_zero = 0
    ending_zero = 0

    for i in range(len(N)):
        if N[i] != "0":
            break 
        leading_zero += 1
    for j in reversed(range(len(N))):
        if N[j] != "0":
            break
        ending_zero += 1 

    if leading_zero > ending_zero:
        print("No")
        return 
    N = "0"*(ending_zero-leading_zero)+N
    # print(leading_zero, ending_zero, N)

    if is_palindrome(N):
        print("Yes")
    else:
        print("No")

main()

