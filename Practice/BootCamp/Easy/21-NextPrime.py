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

def main():
    X = int(input())
    ans = X
    while True:
        if isprime(ans):
            break 
        else:
            ans += 1
    print(ans)

main()