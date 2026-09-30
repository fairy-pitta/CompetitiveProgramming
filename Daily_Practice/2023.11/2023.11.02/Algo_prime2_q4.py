
# This is a template to use on solving problems 

## inputs 
def is_int(): return int(input())
def is_map(type): return map(type, input().split())
def to_list(): return [int(i) for i in list(input())]

## frequently used functions 
from math import sqrt, ceil, floor 




# judge if i is prime for all integer i between 1 and N
# returns a boolean list of [0, N+1] with prime number being True

def Eratosthenes(N: int) -> list:
    isprime = [True] * (N+1)
    # 0 and 1 are not prime numbers 
    isprime[0], isprime[1] = False, False

    for p in range(2, N+1):
        # if its already a composite number, skip
        if not isprime[p]: continue

        q = p * 2
        while q <= N:
            isprime[q] = False
            q += p
        
    return isprime

def main():
    N = is_int()
    isprime = Eratosthenes(N)
    ans = 0
    for i in range(len(isprime)-2):
        if isprime[i] and isprime[i+2]:
            ans += 1
    
    return ans 

print(main())

