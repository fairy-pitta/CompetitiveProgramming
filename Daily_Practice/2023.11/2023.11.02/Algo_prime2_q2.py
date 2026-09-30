from math import sqrt, ceil

def isprime(N):
    flag = True
    if N == 1: return False
    if N == 2: return True
    
    for i in range(ceil(sqrt(N))+1):
        if i <= 1: continue
        elif N%i == 0: 
            flag = False
    return flag 


N = 100

def main(N):
    li = [True for _ in range(100)]
    for i in range(1, N+1):
        if i%2 == 0:
            li[i-1] = False
        elif i%3 == 0:
            li[i-1] = False
        elif i%5 == 0:
            li[i-1] = False
        elif isprime(i):
            li[i-1] = False 
    
    li[0] = False
    return sum(li)

print(main(N))

