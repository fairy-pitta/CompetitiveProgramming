
# This is a template to use on solving problems 

## inputs 
def is_int(): return int(input())
def is_map(type): return map(type, input().split())
def to_list(): return [int(i) for i in list(input())]

## frequently used functions 
from math import sqrt, ceil, floor 


def main():
    N, K = is_map(int)
    S = list(input())

    cnt = 0

    ans = ""

    for i in range(N):
        if cnt >= K:
            ans += "x"
        elif S[i] == "o":
            ans += "o"
            cnt += 1
        else:
            ans += "x"
    
    print(ans)

main()
