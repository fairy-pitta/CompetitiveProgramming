
# This is a template to use on solving problems 

## inputs 
def is_int(): return int(input())
def is_map(type): return map(type, input().split())
def to_list(): return [int(i) for i in list(input())]

## frequently used functions 
from math import sqrt, ceil, floor 
from collections import defaultdict, deque

def shift_list_one_right(lst):
    deque_list = deque(lst)
    deque_list.rotate(1)
    return deque_list

def main():
    N, M = is_map(int)
    S = list(input()) 
    C = list(is_map(int))

    d = defaultdict(deque)
    for i in range(N):
        d[C[i]].append(S[i])
    
    for j in range(len(d)):
        d[j] = shift_list_one_right(d[j])
    
    ans = ["0" for _ in range(N)]
    for k in range(N):
        ans[k] = d[C[k]].popleft()
    
    ans = "".join(ans)
    print(ans)


main()


