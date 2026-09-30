
# This is a template to use on solving problems 

## inputs 
def is_int(): return int(input())
def is_map(type): return map(type, input().split())
def to_list(): return [int(i) for i in list(input())]

## frequently used functions 
from math import sqrt, ceil, floor 

letters_list = [chr(ord('a') + i) for i in range(8)]


def main():
    ans = ""
    for i in range(8):
        s = list(input())
        for j in range(8):
            if s[j] == "*":
                # print(i, j)
                ans += letters_list[j]
                ans += str(8-i)
                
    return ans

print(main())
            