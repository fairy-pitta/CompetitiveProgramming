
# This is a template to use on solving problems 

## inputs 
def is_int(): return int(input())
def is_map(type): return map(type, input().split())
def to_list(): return [int(i) for i in list(input())]

## frequently used functions 
from math import sqrt, ceil, floor 


def main():
    t = is_int()
    for _ in range(t):
        n = is_int()
        s = list(input())

        print(s[-1])

main()

