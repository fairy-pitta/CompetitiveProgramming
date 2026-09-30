
# This is a template to use on solving problems 

## inputs 
def is_int(): return int(input())
def is_map(type): return map(type, input().split())
def to_list(): return [int(i) for i in list(input())]

## frequently used functions 
from math import sqrt, ceil, floor 


def main():
    N = int(input())
    list_set = set()
    for i in range(N):
        li = tuple(list(is_map(int)))
        list_set.add(li)
    print(len(list_set))

main()
