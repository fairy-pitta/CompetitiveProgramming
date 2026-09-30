from math import gcd

def main():
    A, B, K = map(int, input().split())
    n = gcd(A, B)
    if K > max(A, B):
        return -1
    elif K % n == 0:
        return "Yes"
    else:
        return "No"

print(main())