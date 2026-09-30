
# This is a template to use on solving problems 

## inputs 
def is_int(): return int(input())
def is_map(type): return map(type, input().split())
def to_list(): return [int(i) for i in list(input())]

## frequently used functions 
from math import sqrt, ceil, floor 


def main():
    N, M = is_map(int)
    ans = []
    for i in range(2**M):
        size = 0
        li = []
        for j in range(M):
            if i & (1<<j) > 0:
                size += 1
                li.append(j+1)
                
        if size == N:
            ans.append(li)
    ans = sorted(ans)
    for k in ans:
        print(*k)

main()
