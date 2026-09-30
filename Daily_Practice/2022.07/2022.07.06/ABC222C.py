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

# MOD = 998244353
# MOD = 1000000007
# INF = 10 ** 9 + 1 

def main():
    N, M = map(int, input().split())
    A = []
    for _ in range(2*N):
        a = list(input())
        A.append(a)
    rank = [[i, 0] for i in range(1, 2*N+1)]

    for i in range(1, M+1):
        current_rank = rank.copy()
        for k in range(N):
            player1 = current_rank[2*(k+1)-2][0]
            player2 = current_rank[2*(k+1)-1][0]
            player1_hand = A[player1-1][i-1]
            player2_hand = A[player2-1][i-1]
            if player1_hand == player2_hand:
                continue 
            else:
                if (player1_hand == 'G' and player2_hand == "C") or (player1_hand == 'C' and player2_hand == "P") or (player1_hand == "P" and player2_hand == "G"):
                    current_rank[2*(k+1)-2][1] += 1
                else:
                    current_rank[2*(k+1)-1][1] += 1
        rank = sorted(current_rank, key = itemgetter(0))
        rank = sorted(rank, reverse = True, key = itemgetter(1))
        # print(rank)
        
    for player in range(2*N):
        print(rank[player][0])

main()
        

            


