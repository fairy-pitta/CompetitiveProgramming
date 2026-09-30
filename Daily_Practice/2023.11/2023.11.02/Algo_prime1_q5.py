from math import ceil, sqrt
def isprime(N):
    flag = True
    if N == 1: return False
    if N == 2: return True
    
    for i in range(ceil(sqrt(N))+1):
        if i <= 1: continue
        elif N%i == 0: 
            flag = False
    return flag 

def main():
    N = int(input())
    flag = False
    for i in range(N//2+1):
        if isprime(i) and isprime(N-i):
            flag = True
            return i
    
    if not flag:
        return -1

print(main())
    