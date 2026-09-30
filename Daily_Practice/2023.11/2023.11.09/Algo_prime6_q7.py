import math

def my_lcm(x, y):
    return (x * y) // math.gcd(x, y)


def main():
    A, B, K = map(int, input().split())
    lcm = my_lcm(A, B)
    return K * lcm

print(main())
    