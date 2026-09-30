
# This is a template to use on solving problems 

## inputs 
def is_int(): return int(input())
def is_map(type): return map(type, input().split())
def to_list(): return [int(i) for i in list(input())]

## frequently used functions 
from math import sqrt, ceil, floor 
from collections import defaultdict 



def diff():
    n = is_int()
    a = list(is_map(int))
    d = defaultdict(int)

    for i in range(n):
        d[a[i]] += 1
    
    first_num = 0
    second_num = 0

    for key, value in d.items():
        if first_num != 0 and second_num != 0:
            break 
        if value >= 2:
            if first_num == 0:
                first_num = key 
            else:
                second_num = key 
    
    b = [(0) for _ in range(n)]

    if first_num == 0 or second_num == 0:
        print(-1)
        return 

    count_first = 0
    count_second = 0

    for j in range(n):
        if d[a[j]] == 1:
            b[j] = 1
        elif d[a[j]] >= 2 and a[j] == first_num:
            if count_first == 0:
                b[j] = 1
                count_first = 1
            elif count_first == 1:
                b[j] = 2
                count_first = 2
            else:
                b[j] = 1
        elif d[a[j]] >= 2 and a[j] == second_num:
            if count_second == 0:
                b[j] = 1
                count_second = 1
            elif count_second == 1:
                b[j] = 3
                count_second = 2
            else:
                b[j] = 1
        else:
            b[j] = 1
    
    print(*b)
    return


def main():
    t = int(input())
    for _ in range(t):
        diff()

main()    

