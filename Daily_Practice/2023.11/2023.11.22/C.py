
# This is a template to use on solving problems 

## inputs 
def is_int(): return int(input())
def is_map(type): return map(type, input().split())
def to_list(): return [int(i) for i in list(input())]

## frequently used functions 
from math import sqrt, ceil, floor 
from itertools import permutations


def main():
    N = is_int()
    P = list(is_map(int))
    P_list = sorted(list(permutations(P)))
    # print(P_list)
    for i in range(1, len(P_list)):
        if list(P_list[i]) == P:
            print(*P_list[i-1])

main()
