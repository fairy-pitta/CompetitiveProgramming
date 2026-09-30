from collections import Counter

def main():
    N = int(input())
    A = list(map(int, input().split()))
    C = Counter(A)
    ans = 0
    A_max = 2 * 10 ** 5 
    for denom in range(1, A_max+1):
        for nume in range(denom, A_max+1, denom):
            k = nume // denom
            ans += C[denom] * C[nume] * C[k]
    
    return ans 

print(main())


