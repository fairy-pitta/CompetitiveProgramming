
# This is a template to use on solving problems 

## inputs 
def is_int(): return int(input())
def is_map(type): return map(type, input().split())
def to_list(): return [int(i) for i in list(input())]

## frequently used functions 
from math import sqrt, ceil, floor 



S = list(input())
flag = True 
if len(S) != 8: flag = False
else:
    if not S[0].isupper(): flag = False
    if not S[-1].isupper(): flag = False

    for i in range(1, 7):
        if i == 1 and S[i].isnumeric() and int(S[i]) == 0:
            flag = False
        if not S[i].isnumeric():
            flag = False

if flag:
    print("Yes")
else:
    print("No")

