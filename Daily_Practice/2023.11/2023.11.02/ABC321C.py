

# This is a template to use on solving problems 

## inputs 
def is_int(): return int(input())
def is_map(type): return map(type, input().split())
def to_list(): return [int(i) for i in list(input())]

## frequently used functions 
from math import sqrt, ceil, floor 

def like_number() -> list:
    like_number_list = []
    for i in range(2**10):
        num = []
        for j in range(10):
            if i&(1<<j) > 0:
                num.append(j)
        num = sorted(num, reverse = True)
        
        
        result = 0
        for digit in num:
            result = result * 10 + digit
        
        like_number_list.append(result)
    
    return sorted(like_number_list)

def main():
    K = is_int()
    li = like_number()
    print(li[K+1])

main()



