
# This is a template to use on solving problems 

## inputs 
def is_int(): return int(input())
def is_map(type): return map(type, input().split())
def to_list(): return [int(i) for i in list(input())]

## frequently used functions 
from math import sqrt, ceil, floor 


def main():
    S = list(input())
    T = list(input())

    unicode_S = [ord(char) for char in S]
    unicode_T = [ord(char) for char in T]

    ans = True 
    diff = (unicode_S[0] - unicode_T[0]) % 26
    # mod_diff = diff + 26
    #print(diff, mod_diff)
    # print(diff)



    for i in range(len(S)):
        # print(unicode_S[i] - unicode_T[i])
        if (unicode_S[i] - unicode_T[i]) % 26 != diff:
            ans = False
    
    if ans:
        print("Yes")
    else:
        print("No")

main()