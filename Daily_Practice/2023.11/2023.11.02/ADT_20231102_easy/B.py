

# This is a template to use on solving problems 

## inputs 
def is_int(): return int(input())
def is_map(type): return map(type, input().split())
def to_list(): return [int(i) for i in list(input())]

## frequently used functions 
from math import sqrt, ceil, floor 


def main():
    H, W = is_map(int)
    R, C = is_map(int)

    ans = 0

    if H == 1:
        ans += 0
    elif R == 1 or R == H:
        ans += 1 
    else: ans += 2

    if W == 1:
        ans += 0
    elif C == 1 or C == W:
        ans += 1
    else: ans += 2

    print(ans)
    return

main()