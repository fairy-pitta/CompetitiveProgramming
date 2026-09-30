
# This is a template to use on solving problems 

## inputs 
def is_int(): return int(input())
def is_map(type): return map(type, input().split())
def to_list(): return [int(i) for i in list(input())]

## frequently used functions 
from math import sqrt, ceil, floor 

def main():
    N = is_int()
    names = []
    for i in range(N):
        s1, s2 = is_map(str)
        names.append([s1, s2])
    
    for first in range(N):
        for second in range(first+1, N):
            if (names[first][0] == names[second][0] and\
                names[first][1] == names[second][1]):
                return True
    
    return False

if main():
    print("Yes")
else:
    print("No")


