
# This is a template to use on solving problems 

## inputs 
def is_int(): return int(input())
def is_map(type): return map(type, input().split())
def to_list(): return [int(i) for i in list(input())]

## frequently used functions 
from math import sqrt, ceil, floor


def main():
    N = int(input())
    A = list(is_map(int))

    min_A = sum(A) // len(A)
    max_A = sum(A) // len(A) + 1

    move_up = 0
    move_down = 0
    
    for i in range(N):
        if A[i] < min_A:
            move_up += (min_A - A[i])
        elif A[i] > max_A:
            move_down += (A[i] - max_A)
    
    if N == 1:
        return 0
    else:
        return max(move_up, move_down)

print(main())

